import requests
from urllib.parse import parse_qs
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hazard
from .serializers import HazardSerializer
from django_filters import rest_framework as filters
from neighbourhood.filters import EventFilter
from rest_framework.permissions import AllowAny 
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from rest_framework.permissions import AllowAny



API_KEY = 'MzWyPi184rI9oqukYqLChksChNA4cSabhLTWxUGIE5SnY89rpmRKTkGBgG5arsWVsKhfaQR6LzMmkc9DLQLdQx91P5wUcpS_wlUhg-zZvoL7QYorY6jwF4e20Ry3WnYx'

API_HOST = 'https://api.yelp.com'
EVENT_PATH = '/v3/events/'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

def yelp_request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    return createResponse(response.json())

createResponse = lambda data: Response(
    data,
    status = status.HTTP_200_OK,
    headers = { "Content-Type": "application/json; charset=utf-8" }
)

class YelpEventsView(APIView):
    permission_classes = AllowAny,
    def get(self, request):
        url_params = {
        'longitude': request.GET.get('longitude', ''),
        'latitude': request.GET.get('latitude', ''),
        'categories': request.GET.get('categories', ''),
        'limit': 50,
        'radius': 4000
        }
        return yelp_request(API_HOST, EVENT_PATH, API_KEY, url_params=url_params)

class YelpSearchView(APIView):
    permission_classes = AllowAny,
    def get(self, request):
        url_params = {
        'longitude': request.GET.get('longitude', ''),
        'latitude': request.GET.get('latitude', ''),
        'categories': request.GET.get('categories', ''),
        'limit': 50,
        'radius': 1200
        }
        return yelp_request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)


class YelpBusinessView(APIView):
    permission_classes = AllowAny,
    def get(self, request):
        url_params = {
        'longitude': request.GET.get('longitude', ''),
        'latitude': request.GET.get('latitude', ''),
        'radius': 4000
        }
        return yelp_request(API_HOST, BUSINESS_PATH, API_KEY, url_params=url_params)




class HazardList(generics.ListAPIView):
    queryset = Hazard.objects.all()
    serializer_class=HazardSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EventFilter
    permission_classes = AllowAny,

    
    
    
    

    
    
