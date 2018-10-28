from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.block_select,name='block_select'),
    url(r'^(?P<block>\w+)/$',views.floor_select,name='floor_select'),
    url(r'^(?P<block>\w+)/(?P<floor>\d+)/$',views.room_select,name='room_select'),
    url(r'^details/(?P<id>\d+)/$',views.details,name='details')
]