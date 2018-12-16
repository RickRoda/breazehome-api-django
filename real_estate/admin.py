from django.contrib import admin
from real_estate.models import (Property,
                                PropertyMedia,
                                PropertyDetail,
                                List)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
