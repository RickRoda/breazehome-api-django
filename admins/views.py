import rest_framework
from rest_framework import generics, status, viewsets, filters, permissions, response
from rest_framework.views import APIView
import json
from datetime import date
from datetime import time
import datetime
import calendar

from rest_framework.permissions import AllowAny

from admins.serializers import (ThemesSerializer,
                              ConfigurationSerializer,
                              PropertyFilterSerializer)
from admins.models import (Themes,
                          Configuration,
                          PropertyFilter)

class BackupView(APIView):
  """
  Get the backup configuration file as jason
  """
  permission_classes = AllowAny,
  def get(self, request, format=None):
    try:
      with open('backup/backup_config.json') as f:
        data = json.load(f)
    except:
      data = {
        "archived": 8,
        "day": calendar.day_name[date.today().weekday()],
        "hour": 3
      }
    return response.Response({ "success": True, "content": data })

  """
  Update the backup configuration file
  """
  def put(self, request, format=None):
    try:
      with open('backup/backup_config.json', 'w') as f:
        json.dump(request.data, f)
      return response.Response({ "success": True, "content": request.data })
    except:
      return response.Response({ "success": False, "content": request.data })

class ThemesViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    ordering_fields = '__all__'
    serializer_class = ThemesSerializer
    permission_classes = AllowAny,

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    ordering_fields = '__all__'
    serializer_class = ConfigurationSerializer
    permission_classes = AllowAny,


class PropertyFilterViewSet(viewsets.ModelViewSet):
    queryset = PropertyFilter.objects.all()
    ordering_fields = '__all__'
    serializer_class = PropertyFilterSerializer
    permission_classes = AllowAny,

