from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'telphone', 'language', 'currency')


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    # provider = ProviderSerializer(read_only=True)

    class Meta:
        model = ServiceArea
        geo_field = 'area'
        fields = ('id', 'name', 'price', 'provider')
