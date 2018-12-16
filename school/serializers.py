
from school.models import Schools
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schools
		fields = '__all__'
