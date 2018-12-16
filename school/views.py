
from school.models import Schools
from school.serializers import (SchoolSerializer,)

from rest_framework.decorators import api_view,detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class SchoolViewSet(viewsets.ModelViewSet):
	queryset = Schools.objects.all()
	serializer_class = SchoolSerializer
