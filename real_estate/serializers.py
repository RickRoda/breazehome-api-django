from real_estate.models import (Agent,
                                Property,
                                PropertyMedia,
                                PropertyDetail,
                                PropertyViewCount,
                                PropertyLocation,
                                FavProperty,
                                Board,
                                Theme,
                                List,
                                Tag,
                                SavedSearch,
                                OpenHouse,
                                BHGeometry,
                                SearchHistory)
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from rest_framework_gis.serializers import GeometryField


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    location_point = PointField()
    class Meta:
        model = Property
        fields = '__all__'

        
class FavPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavProperty
        fields = '__all__'
        
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        

class PolygonSerializer(serializers.Serializer):
    """ A class to serialize locations as GeoJSON compatible data """
    # a field which contains a geometry value and can be used as geo_field
    polygon = GeometryField()
    area = serializers.CharField(max_length=200)


class PropertyMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMedia
        fields = '__all__'


class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetail
        fields = '__all__'

class PropertyViewCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViewCount
        fields = '__all__'


class PropertyLocationSerializer(serializers.ModelSerializer):
    point = PointField()
    class Meta:
        model = PropertyLocation
        fields = '__all__'

class PropertyTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    property_objects = serializers.SerializerMethodField()

    def get_property_objects(self, _list):
        property_objects = Property.objects.filter(pk__in=_list.properties.all())
        serialized = PropertySerializer(property_objects,
                context={'request':self.context.get('request')},
                many=True
        )
        return serialized.data

    class Meta:
        model = List
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class SavedSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSearch
        fields = '__all__'

class OpenHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHouse
        fields = '__all__'

class BHGeometrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BHGeometry
        fields = '__all__'

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'
