from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Provider, ServiceArea


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telphone', 'language', 'currency')


@admin.register(ServiceArea)
class ServiceAreaAdmin(OSMGeoAdmin):
    list_display = ('name', 'price', 'area')
