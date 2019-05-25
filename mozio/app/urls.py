from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import ProviderViewSet, ServiceAreaViewSet


router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet)
router.register(r'service_area', ServiceAreaViewSet)

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    url(r'^docs$', schema_view),
    url(r'^', include(router.urls)),
]
