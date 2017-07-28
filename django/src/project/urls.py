from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

from .views import MarkViewSet

router = routers.DefaultRouter()
router.register(r'mark', MarkViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
]
