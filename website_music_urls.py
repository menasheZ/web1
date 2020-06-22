from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('music1/', views.index1, name='index1'),

    # /music/71/
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name="detail"),

    # /music/71/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
]
