from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.reviews),
    url(r'^review_updates/(?P<uuid>[^/]+)$', views.review_update),
    url(r'^movie_reviews/', views.movie_reviews),
    url(r'^movie_reviews_name/(?P<uuid>[^/]+)$', views.movie_reviews_name),
]