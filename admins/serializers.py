from rest_framework import serializers
from .models import (Themes,
                    Configuration,
                    PropertyFilter)

class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'




class PropertyFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFilter
        fields = '__all__'


