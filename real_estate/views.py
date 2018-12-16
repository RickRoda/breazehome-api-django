from django.conf import settings
from django.utils import timezone
import rest_framework
import datetime
from rest_framework import generics, status, viewsets, filters, permissions, response
from rest_framework.permissions import AllowAny

from real_estate.serializers import (AgentSerializer,
                                     PropertySerializer,
                                     PropertyMediaSerializer,
                                     PropertyDetailSerializer,
                                     PropertyViewCountSerializer,
                                     PropertyLocationSerializer,
                                     PropertyTagSerializer,
                                     FavPropertySerializer,
                                     BoardSerializer,
                                     ThemeSerializer,
                                     ListSerializer,
                                     SavedSearchSerializer,
                                     OpenHouseSerializer,
                                     BHGeometrySerializer,
                                     SearchHistorySerializer)
from real_estate.mixins import AllowPUTAsCreateMixin
from real_estate.models import (Agent,
                                Property,
                                PropertyMedia,
                                PropertyDetail,
                                PropertyViewCount,
                                PropertyLocation,
                                FavProperty,
                                Board,
                                Tag,
                                Theme,
                                List,
                                SavedSearch,
                                OpenHouse,
                                BHGeometry,
                                SearchHistory)
from admins.models import Configuration

from real_estate.filters import (PropertyFilter,
                                 SavedSearchFilter,
                                 SearchHistoryFilter)

from rest_framework.decorators import list_route,detail_route
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.response import Response
from real_estate.filters import (PropertyFilter)
from rest_framework.decorators import list_route
from django.contrib.gis.geos import GEOSGeometry
from django.db.models import Count
from django.db.models.query import EmptyQuerySet
from itertools import chain
from django.db.models import Q
import urllib
import json
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination
from real_estate.polygons import Polygons
from real_estate.utilities import Utilities
import sys
from django.forms import ModelForm


# BEGIN Import Django email lib: Adrian ahern471@fiu.edu
from django.core.mail import send_mail
from breaze.settings import EMAIL_HOST_USER
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.context_processors import request
from django.views.generic import detail
from django.shortcuts import get_object_or_404


# END Import Django email lib

# START search engine:acris005@fiu.edu
from real_estate.search import SearchEngine
# END search engine

class AgentViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = AgentSerializer
    ordering_fields = '__all__'
    pagination_class = None
    queryset = Agent.objects.all()

class PropertyViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows properties to be viewed or edited.

    Sub resource are PropertyMedia and PropertyDetail which can be found at
    `/property/{id}/media` and `/property/{id}/detail` respectively.

    Fields with filters enabled are:

    ```
      1. 'current_price'
      2. 'beds_total'
      3. 'for_sale_yn'
      4. 'for_lease_yn'
      5. 'property_type'
      6. 'matrix_unique_id'
      7. 'sq_ft_total'
      8. 'year_built'
      9. 'lot_sq_footage'
      10. 'pets_allowed_yn'
      11. 'status'
      12. 'city'
      13. 'location_point'
      14. 'address_internet_display'
      15. 'postal_code'
      16. 'state_or_province'
      17. 'baths_full'
      18. 'baths_half'
      19. 'property_sq_ft'
      20. 'internet_yn'
      21. 'pool_yn'
      22. 'balcony_porchandor_patio_yn'
    ```
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    ordering_fields = '__all__'
    filter_class = PropertyFilter
    pagination_class = LimitOffsetPagination
    # START API authentication: erosa044@fiu.edu
    permission_classes = AllowAny,
    # END API authentication


    #Ashif's Code . Merge this Overridden get_queryset method only , ignore other new methods below this .
    """
        Overwrite get queryset to check if get openhouse only
    """
    # START search engine:acris005@fiu.edu
    def get_queryset(self):
        """
        name: get_queryset
        goal: prepare queryset, get query from frontend, start search engine
        out:  returns a filtered queryset from the search engine
        """

        queryset = super().get_queryset()
        query = self.request.query_params.get('address', None)

        if query:
            search_engine = SearchEngine(query, queryset)
            queryset = search_engine.start()

        return queryset
    # END search engine

    #BEGIN PoLR Search API Implementation
    """
        Takes a search text query string and returns a list of possible suggestions after geographically whittling down the list to properties reachable in a certain amount of time, from a certain place, on a given day/time of the week
    """
    @list_route()
    def polr_properties(self, request):

        polr_settings = Configuration.objects.get(pk=1)

        #as of 11/5, the snippet below is the following isochrone:  Thurs, 5 PM, 25 mins (12 Angle Resolution), 11200 SW 8th St, Miami, FL 33199
        #isochrone = GEOSGeometry('POLYGON((-80.3751759 25.911687097606865,-80.28473648804989 25.898918989833717,-80.24774816235096 25.824201546038474,-80.19851276692452 25.757927101646676,-80.28230525890234 25.709693429825073,-80.30593866521605 25.6499125259134,-80.3751759 25.514045693396184,-80.44486951364652 25.649199082665632,-80.48802435212174 25.699281908971468,-80.62076348098006 25.7578276979772,-80.49289227745373 25.819165354409773,-80.42851107061833 25.841165849790585,-80.3751759 25.911687097606865))')
        isochrone = GEOSGeometry("POLYGON((" + request.GET.get('polr', "") + "))")

        polr_properties = Property.objects.filter(location_point__coveredby=isochrone)

        # get price filter range parameters
        price_high = request.GET.get('current_price__lte')
        price_low = request.GET.get('current_price__gte')

        #use values to filter by price range
        polr_properties = polr_properties.filter(current_price__lte=price_high)
        polr_properties = polr_properties.filter(current_price__gte=price_low)


        #dyanmic filter stacker except  polr and price
        for key, value in request.GET.items():
            if str(key) != "polr" and str(key) != "current_price__lte" and key != "current_price__gte":
                command = "polr_properties = polr_properties.filter(" + str(key) + "=" + str(value) + ")\n"
               # sys.stderr.write(command)
                exec(command, globals(), locals())

        serializer = PropertySerializer(polr_properties, many=True)

        page = self.paginate_queryset(polr_properties)
        if page is not None:
            serializer = PropertySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return response.Response(serializer.data)

    #END PoLR Search API Implementation

    """
        Takes a polygon with longitude and then latitude
    """
    @list_route()
    def poly_properties(self, request):
        #geom = GEOSGeometry('POLYGON(( -80.3653335571289 25.743003105825977, -80.23761749267578 25.743003105825977,-80.23761749267578 25.82523468800373,-80.3653335571289 25.82523468800373,-80.3653335571289 25.743003105825977))')
        geom = GEOSGeometry(request.query_params['poly'])
        #poly_properties = PropertyLocation.objects.filter(point__coveredby=geom)
        poly_properties = Property.objects.filter(location_point__coveredby=geom)
        #serializer = PropertyLocationSerializer(poly_properties, many=True)
        serializer = PropertySerializer(poly_properties, many=True)

        page = self.paginate_queryset(poly_properties)
        if page is not None:
            #serializer = PropertyLocationSerializer(page, many=True)
            serializer = PropertySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return response.Response(serializer.data)

    """
        Takes a search text query string and returns a list of possible suggestions
    """
    @list_route()
    def search_location_ajax(self, request):

        address = request.GET.get('address', "") #request.query_params['address']
        zipcode = request.GET.get('zip', "") #request.query_params['zip']
        city = request.GET.get('city', "") #request.query_params['city']
        #state = request.GET.get('state',"")
        properties = {}
        if len(address) > 1 and len(zipcode) > 1 and len(city) > 1:
            properties = Property.objects.filter( (Q(address_internet_display__istartswith=address) & Q(city__istartswith=city) & Q(postal_code__istartswith=zipcode)) ).values("address_internet_display", "city", "postal_code", "state_or_province")
        elif len(address) > 1 and len(zipcode) > 1:
            properties = Property.objects.filter( (Q(address_internet_display__istartswith=address) & ~Q(city__iexact=city) & Q(postal_code__istartswith=zipcode)) ).values("address_internet_display", "city", "postal_code", "state_or_province")
        elif len(city) > 1 and len(zipcode) > 1:
            properties = Property.objects.filter( (~Q(address_internet_display__iexact=address) & Q(city__istartswith=city) & Q(postal_code__istartswith=zipcode)) ).values("address_internet_display", "city", "postal_code", "state_or_province").distinct("city")
        elif len(address) > 1 and len(city) > 1:
            properties = Property.objects.filter( (Q(address_internet_display__istartswith=address) & Q(city__istartswith=city) & ~Q(postal_code__iexact=zipcode)) ).values("address_internet_display", "city", "postal_code", "state_or_province")
        elif len(address) > 1:
            properties = Property.objects.filter( (Q(address_internet_display__istartswith=address) & ~Q(city__iexact=city) & ~Q(postal_code__iexact=zipcode)) ).values("address_internet_display", "city", "postal_code", "state_or_province")
        elif len(city) > 1:
            properties = Property.objects.filter( (~Q(address_internet_display__iexact=address) & Q(city__istartswith=city) & ~Q(postal_code__iexact=zipcode)) ).values("city", "postal_code", "state_or_province").distinct("city")
        elif len(zipcode) > 1:
            properties = Property.objects.filter( (~Q(address_internet_display__iexact=address) & ~Q(city__iexact=city) & Q(postal_code__istartswith=zipcode)) ).values("city", "postal_code", "state_or_province").distinct("city")

        return JsonResponse({'suggestions': list(properties)})

    # BEGIN Share property via email: Adrian ahern471@fiu.edu
    @list_route()
    def share_via_email(self, request):

        print('share_via_email called')

        if request.method == "GET":

            recipient_email = request.GET.get('recipient_email', "")
            sender_email    = request.GET.get('sender_email', "")
            email_body      = request.GET.get('email_body', "")
            property_url    = request.GET.get('property_url', "")
            subject         = sender_email + ' shared a home on BreazeHome'

            # email_body = email_body + ' ' + property_url

            print('email body = ' + email_body)
            print('sender email = ' + sender_email)
            print('recipient email = ' + recipient_email)

        else:
            # bad request
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Create the body of the message (a plain-text and an HTML version).

        html = """\
             <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Shared Listing</h1>
                    <p><b>""" + '"' + email_body + '"' + """</b></p>
                    <p><a href=""" + property_url + """ target="_top">See on Breaze Home</a></p><br><br>
                    <p style="color:gray;"><font size="3">Shared by:</font></p>
                    <p><a href="mailto:""" + sender_email + '"'+ """ target="_top">"""+sender_email + """</a></p>
                </body>
            </html>

        """
        print(html)
        send_mail(
            subject,
            email_body,
            EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
            html_message=html
        )

        return Response(status=status.HTTP_200_OK)
    # END Share property via email

# START #2487 AND #2357 Andreina Rojas aroja108@fiu.edu
class FavPropertyViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    queryset = FavProperty.objects.all()
    serializer_class = FavPropertySerializer
    ordering_fields = '__all__'
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    @list_route()
    def properties(self,request):
       filters = []
       puser = request.GET.get ('puser')
       objs = FavProperty.objects.filter(user=puser)
       
       for obj in objs:
           prop = obj.property.id
           filters.append(prop)
               
       allp = Property.objects.filter(id__in = filters)
       
       serializer = PropertySerializer(allp, many=True)
       return Response(serializer.data)

    @list_route()
    def isSaved(self,request):
        pid = request.GET.get('pid')
        puser = request.GET.get ('puser')

        try:
            obj = FavProperty.objects.filter(property = pid, user = puser)
        except FavProperty.DoesNotExist:
            obj = None

        if obj is not None:
            serializer= FavPropertySerializer(obj, many=True)
            return Response(serializer.data)




    @list_route()
    def unfavorite(self,request):
        pid = request.GET.get('pid')
        puser = request.GET.get ('puser')
        obj = FavProperty.objects.get(property = pid, user = puser)
        obj_query = FavProperty.objects.filter(id=obj.id)
        serializer = FavPropertySerializer(obj_query, many=True)
        obj_query.delete()
        return response.Response(serializer.data)



    @detail_route(methods=['POST'])
    def save(self, request):
        userf = request.POST.get('user')
        propertyf = request.POST.get('property')
        FavProperty.objects.create(
            user = userf,
            property = propertyf)


        return response.Response(serializer.data)


class BoardViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    ordering_fields = '__all__'
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    @list_route()
    def getUserBoards(self,request):
        puser = request.GET.get('puser')

        objs = Board.objects.filter(user = puser)
        objs = objs.distinct('name')

        serializer = BoardSerializer(objs, many=True)
        return Response(serializer.data)

    @list_route()
    def getPropertiesInBoard(self,request):
        filter = []
        nameb = request.GET.get('name')
        objs = Board.objects.filter(name=nameb)

        for obj in objs:
            filter.append(obj.property.id)

        props = Property.objects.filter(id__in = filter)
        serializer = PropertySerializer(props, many=True)
        return Response(serializer.data)

    @list_route()
    def deletePropBoard(self,request):
        nameb = request.GET.get('name')
        pid = request.GET.get('property')
        puser = request.GET.get('puser')

        obj_query = Board.objects.filter(name = nameb, user = puser, property = pid)
        serializer = BoardSerializer(obj_query, many=True)
        obj_query.delete()

        return Response(serializer.data)

    @list_route()
    def deleteBoard(self,request):
        puser = request.GET.get('puser')
        nameb = request.GET.get('name')

        obj_query = Board.objects.filter(name = nameb, user = puser)
        serializer = BoardSerializer(obj_query, many=True)
        obj_query.delete()
        return Response(serializer.data)

    @list_route()
    def rename(self,request):
        puser = request.GET.get('puser')
        nameb = request.GET.get('name')
        newnameb = request.GET.get('newname')

        obj_query = Board.objects.filter(name = nameb, user = puser)
        serializer = BoardSerializer(obj_query, many=True)
        obj_query.update(name = newnameb)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def boardsave(self, request):
        nameb = request.POST.get('name')
        userb = request.POST.get('user')
        idp = request.POST.get('property')


        Board.objects.create(
                name = nameb,
                user = userb,
                property = idp)


        return response.Response(serializer.data)


# END #2487 AND #2357 Andreina Rojas aroja108@fiu.edu


class PropertyDetailViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = PropertyDetailSerializer
    ordering_fields = '__all__'
    pagination_class = None
    permission_classes = AllowAny,

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        return PropertyDetail.objects.filter(property=pk)

#START View Competition for Properties : adubu002@fiu.edu

class PropertyUpdateCountViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = PropertyViewCountSerializer
    ordering_fields = '__all__'
    pagination_class = None
    permission_classes = AllowAny,

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        obj, created = PropertyViewCount.objects.get_or_create(
            property=Property.objects.get(id=pk),
        )

        #gets propertyViewCount table entry using the property as the id
        entry = PropertyViewCount.objects.get(property=pk)

        #increments the total count and recalulates the weekly count
        self.increment_count(entry)

        #saves changes to entry to the propertyViewCount table
        entry.save()

        #gets property table entry by id
        entry2 = Property.objects.get(id=pk)

        #increments the total view count of the property
        entry2.count = entry.total_count

        #saves changes to entry in the property table
        entry2.save()
        return PropertyViewCount.objects.filter(property=pk)

    #increments the total view counts and recalulates the weekly view counts
    #of a propertyviewcount entry
    def increment_count(self, entry):
        entry.total_count += 1

        #variable that stores the current day of the week (0-6)
        weekday = datetime.datetime.today().weekday()

        #variable that holds the current datetime object using
        today = timezone.now()

        #depending on the day of the week a method is called to increment update
        #the view count for that day
        if weekday == 0:
            self.monday(entry, today)
        elif weekday == 1:
            self.tuesday(entry, today)
        elif weekday == 2:
            self.wednesday(entry, today)
        elif weekday == 3:
            self.thursday(entry, today)
        elif weekday == 4:
            self.friday(entry, today)
        elif weekday == 5:
            self.saturday(entry, today)
        elif weekday == 6:
            self.sunday(entry, today)

        #the sum of all the daily counts for the past 7 days is stored in this variable
        entry.weekly_count = self.weekly_sum(entry, today)

    #calucales the view count for the past seven days with regard to the today
    #varibale which is passed intot eh function
    def weekly_sum(self, entry, today):
        result = 0

        #dictionary of weekdays dates to weekday views
        week = {
            entry.mon_date : entry.mon_count,
            entry.tues_date : entry.tues_count,
            entry.wed_date : entry.wed_count,
            entry.thurs_date : entry.thurs_count,
            entry.fri_date : entry.fri_count,
            entry.sat_date : entry.sat_count,
            entry.sun_date : entry.sun_count
        }

        #margin object stores the range of dates within 7 days of the current date
        margin = datetime.timedelta(days = 7)

        #loops through the dictionary shown above and only adds the weekday view counts
        #to the results tally if the weekday date is within the margin of dates indictated
        #by the margin object
        for day in week:
            if today - margin <= day:
                result += week[day]
        return result

    def monday(self, entry, today):
        #if entry does not exist a new entry is created
        if entry.mon_date == None:
            entry.mon_date = today
        #if the date sent into the function matches the date in the database then
        #the view count for that date is incremented
        elif today.date() == entry.mon_date.date():
            entry.mon_count += 1
        #if the date passed into the function does not match the dae in the database
        #then the date in the database is changed to the current date and the view
        #count is set to 1
        else:
            entry.mon_count = 1
            entry.mon_date = today

    def tuesday(self, entry, today):
        if entry.tues_date == None:
            entry.tues_date = today
        elif today.date() == entry.tues_date.date():
            entry.tues_count += 1
        else:
            entry.tues_count = 1
            entry.tues_date = today

    def wednesday(self, entry, today):
        if entry.wed_date == None:
            entry.wed_date = today
        elif today.date() == entry.wed_date.date():
            entry.wed_count += 1
        else:
            entry.wed_count = 1
            entry.wed_date = today

    def thursday(self, entry, today):
        if entry.thurs_date == None:
            entry.thurs_date = today
        elif today.date() == entry.thurs_date.date():
            entry.thurs_count += 1
        else:
            entry.thurs_count = 1
            entry.thurs_date = today

    def friday(self, entry, today):
        if entry.fri_date == None:
            entry.fri_date = today
        elif today.date() == entry.fri_date.date():
            entry.fri_count += 1
        else:
            entry.fri_count = 1
            entry.fri_date = today

    def saturday(self, entry, today):
        if entry.sat_date == None:
            entry.sat_date = today
        elif today.date() == entry.sat_date.date():
            entry.sat_count += 1
        else:
            entry.sat_count = 1
            entry.sat_date = today

    def sunday(self, entry, today):
        if entry.sun_date == None:
            entry.sun_date = today
        elif today.date() == entry.sun_date.date():
            entry.sun_count += 1
        else:
            entry.sun_count = 1
            entry.sun_date = today


#return viewing data for a specified property
class PropertyViewCountViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = PropertyViewCountSerializer
    ordering_fields = '__all__'
    pagination_class = None

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        obj, created = PropertyViewCount.objects.get_or_create(
            property=Property.objects.get(id=pk),
        )
        return PropertyViewCount.objects.filter(property=pk)

#END View Competition for Properties

class PropertyMediaViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    serializer_class = PropertyMediaSerializer
    ordering_fields = '__all__'
    permission_classes = AllowAny,

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        return PropertyMedia.objects.filter(property=pk)



class PropertyLocationViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows locaitons to be viewed or edited.
    """
    serializer_class = PropertyLocationSerializer
    ordering_fields = '__all__'
    pagination_class = None
    permission_classes = AllowAny,

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        return PropertyLocation.objects.filter(property=pk)

class PropertyTagViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    serializer_class = PropertyTagSerializer
    ordering_fields = '__all__'
    permission_classes = AllowAny,

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['property_pk']
        return Tag.objects.order_by("tag").filter(pid=pk).distinct('tag')

class TagViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    serializer_class = PropertyTagSerializer
    ordering_fields = '__all__'
    queryset = Tag.objects.all()
    permission_classes = AllowAny,

    @list_route()
    def search(self, request):
        tags = request.query_params['tag']
        tag_properties = Tag.objects.filter(tag=tags)
        serializer = PropertyTagSerializer(tag_properties, many=True)

        page = self.paginate_queryset(tag_properties)
        if page is not None:
            serializer = PropertyTagSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return response.Response(serializer.data)

    @list_route()
    def user(self, request):
        tags = request.query_params['tag']
        userid = request.query_params['uid']
        tag_properties = Tag.objects.filter(tag=tags,uid=userid)
        serializer = PropertyTagSerializer(tag_properties, many=True)

        page = self.paginate_queryset(tag_properties)
        if page is not None:
            serializer = PropertyTagSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return response.Response(serializer.data)
class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ListSerializer
    ordering_fields = '__all__'
    permission_classes = AllowAny,

    @detail_route(methods=['POST'])
    def save(self, request, user_pk, pk=None):
        # import ipdb
        # ipdb.set_trace()
        list_instance = List.objects.get(user=user_pk)
        property_instance = Property.objects.get(pk=request.data['property'])
        list_instance.properties.add(property_instance)
        return Response({'status': 'property added'})


    def get_queryset(self):
        """
        This view should return a list of all the List for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['user_pk']
        return List.objects.filter(user=pk)


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    ordering_fields = '__all__'
    serializer_class = ThemeSerializer
    permission_classes = AllowAny,

class SavedSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows searches to be viewed or edited.

    Fields with filters enabled are:

    ```
      1. 'title'
      2. 'price'
      3. 'beds_minimum'
      4. 'property_type'
      5. 'transaction_type'
    ```
    """
    serializer_class = SavedSearchSerializer
    ordering_fields = '__all__'
    filter_class = SavedSearchFilter
    permission_classes = AllowAny,


    def get_queryset(self):
        """
        This view should return a list of all the searches for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['user_pk']
        return SavedSearch.objects.filter(user=pk)

class OpenHouseViewSet(AllowPUTAsCreateMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = OpenHouseSerializer
    ordering_fields = '__all__'
    pagination_class = None
    permission_classes = AllowAny,
    queryset = OpenHouse.objects.all()

#BEGIN PoLR Geometry API Implementation

class BHGeometryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for invocation of geometric utilities.
    """


    serializer_class = BHGeometrySerializer
    ordering_fields = None
    pagination_class = None
    permission_classes = AllowAny,
    queryset = BHGeometry.objects.none()  #this is a service logic ViewSet, hence there will be no results coming from the database for this release

    @list_route()
    def get_geocode(self, request):
        """
        This returns the geocode for a given address string.  It is a wrapper to the internal get_geocode() functionality used for other coding
        and represents a convenience forwarded to API callers for the sake of consitency in the entire API and front ends.
        """
        polr_settings = Configuration.objects.get(pk=1)
        return JsonResponse({ "originGeocode" : Utilities.get_geocode(request.GET.get("origin_address", ""), polr_settings) })

    @list_route()
    def get_polr(self, request):
        """
        This returns the PoLR JSON data structure consisting of a geocode for a given address string and an isochrone represented by all points reachable
        from the origin geocode in the specified travel_duration for a given travel_mode.  The isochrone is formed by connecting isopoints with isolines
        to enclose the area of the polygon.
        """

        polr_settings = Configuration.objects.get(pk=1)
        origin_geocode = Utilities.get_geocode(request.GET.get("origin_address", ""), polr_settings)
        isochrone = Polygons.get_isochrone(origin_geocode, request.GET.get("arrival_datetime", ""), request.GET.get("travel_duration", ""), request.GET.get("travel_mode", "driving"), polr_settings)  #default to driving, add more arguments as necessary here for supporting additional isochrone generation parameters.

        return JsonResponse({"originGeocode" : origin_geocode, "isochrone" : isochrone})

#END PoLR Geometry API Implementation

class SearchHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows searches history to be viewed or edited.

    Fields with filters enabled are:

    ```
      1. 'id'
      2. 'time_created'
      3. 'count'
      4. 'query_string'
    ```
    """
    serializer_class = SearchHistorySerializer
    ordering_fields = '__all__'
    filter_class = SearchHistoryFilter


    def get_queryset(self):
        """
        This view should return a list of all the searches history for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['user_pk']
        return SearchHistory.objects.filter(user=pk)
