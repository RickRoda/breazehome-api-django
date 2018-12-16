from rest_framework import serializers
from county_records.models import CountyRecord, LienRecord
# Richard Roda
# Serializer for the BreazeHome lien search feature

class CountyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountyRecord
        fields = '__all__'

class LienRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LienRecord
        fields = '__all__'