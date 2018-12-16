from django.contrib import admin
from .models import CountyRecord, LienRecord

# Register your models here.
admin.site.register(CountyRecord)
admin.site.register(LienRecord)