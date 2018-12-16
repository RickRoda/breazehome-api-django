from rest_framework import viewsets
import rest_framework_filters as filters
from django_filters import Filter
from django_filters.fields import Lookup
from neighbourhood.models import Hazard
import django_filters
from django_filters import Filter
from django_filters.fields import Lookup
from django.db import models


class EventFilter(filters.FilterSet):

    class Meta:
        model = Hazard
        fields = {
        'YEAR':['gte'],
        'STATE':['iexact'],
        'STATE_FIPS':['exact'],
        'EVENT_TYPE':['icontains'],
        'CZ_TYPE':['iexact'],
        'CZ_FIPS':['exact'],
        'CZ_NAME':['icontains']

        }
