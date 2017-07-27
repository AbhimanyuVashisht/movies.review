from django.conf.urls import url
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^movies/$', views.movies),
    url(r'^movies_name/(?P<uuid>[^/]+)$', views.movies_by_name),
    url(r'^tvshows_id/(?P<uuid>[^/]+)$', views.tvshows_by_id),
]
