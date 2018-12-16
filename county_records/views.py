from django.conf import settings
from rest_framework import generics, status, viewsets, filters, permissions, response
from rest_framework.pagination import PageNumberPagination
from .serializers import CountyRecordSerializer, LienRecordSerializer
from .models import CountyRecord, LienRecord
from .filters import CountyRecordFilter, LienRecordFilter
from rest_framework.permissions import AllowAny
# Richard Roda
# Views for the BreazeHome lien search feature


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CountyRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = CountyRecordSerializer
    ordering_fields = '__all__'
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = CountyRecordFilter
    queryset = CountyRecord.objects.all()
    
class LienRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows details to be viewed or edited.
    """
    serializer_class = LienRecordSerializer
    ordering_fields = '__all__'
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = LienRecordFilter
    queryset = LienRecord.objects.all()
    permission_classes = AllowAny,