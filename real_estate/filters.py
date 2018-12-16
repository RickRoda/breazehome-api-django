from rest_framework import viewsets
import rest_framework_filters as filters
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django.contrib.gis.db import models as gis_models
from real_estate.models import (Property,
                                PropertyMedia,
                                PropertyDetail,
                                List,
                                SavedSearch,
                                SearchHistory)


class PropertyFilter(filters.FilterSet):
    class Meta:
        model = Property
        fields = {
            'current_price': '__all__',
            'beds_total': '__all__',
            'baths_full': '__all__',
            'baths_half': '__all__',
            'for_sale_yn': '__all__',
            'for_lease_yn': '__all__',
            'property_type': '__all__',
            'matrix_unique_id': '__all__',
            'sq_ft_total': '__all__',
            'year_built': '__all__',
            'property_sq_ft': '__all__',
            'lot_sq_footage': '__all__',
            'pets_allowed_yn': '__all__',
            'status': '__all__',
            'city': '__all__',
            'location_point': ['coveredby'],
            'address_internet_display': '__all__',
            'postal_code': '__all__',
            'state_or_province': '__all__',
            'internet_yn': '__all__',
            'pool_yn': '__all__',
            'balcony_porchandor_patio_yn': '__all__'
        }
        filter_overrides = {
            gis_models.PointField: {
                'filter_class': GeometryFilter,
                'extra': lambda f: {
                    'lookup_expr': 'coveredby',
                },
            },
        }

class SavedSearchFilter(filters.FilterSet):
    class Meta:
        model = SavedSearch
        fields = {
            'title': '__all__',
            'query_string': '__all__',
            'id': '__all__'
        }

class SearchHistoryFilter(filters.FilterSet):
    class Meta:
        model = SearchHistory
        fields = {
            'id': '__all__',
            'time_created': '__all__',
            'count': '__all__',
            'query_string': '__all__'
        }
