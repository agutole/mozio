import logging

from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError

from .serializers import ProviderSerializer, ServiceAreaSerializer
from .models import Provider, ServiceArea


logger = logging.getLogger(__name__)


class ProviderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a `Provider` instance.

    list:
        Return all `Provider's`.

    create:
        Create a new `Provider`.

    delete:
        Remove an existing `Provider`.

    partial_update:
        Update one or more fields on an existing `Provider`.

    update:
        Update a `Provider`.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaFilter(filters.FilterSet):
    """
    asdasda
    """

    point = filters.CharFilter(method='filter_point', label='Point',
                               help_text=u'Return areas that contain `point=<longitude>,<latitude>`',
                               type=u'test')

    def filter_point(self, queryset, name, value):
        try:
            latitude, longitude = [float(v) for v in value.split(',')]
            point = Point(longitude, latitude)

        except Exception:
            logger.exception('Can\'t create Point(longitude, latitude) with provided data')
            raise ValidationError('Error on latitude/longitude provided data')

        return ServiceArea.objects.filter(area__contains=point)

    class Meta:
        model = ServiceArea
        fields = ('point',)


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a `ServiceArea` instance. You can filter by a geo point.

    list:
        Return all `ServiceArea`.

    create:
        Create a new `ServiceArea`.

    delete:
        Remove an existing `ServiceArea`.

    partial_update:
        Update one or more fields on an existing `ServiceArea`.

    update:
        Update a `ServiceArea`.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'price',)
    filterset_class = ServiceAreaFilter
