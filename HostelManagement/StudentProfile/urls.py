from django.conf.urls import url
from . import views

app_name ="profiles" 

urlpatterns = [
    url(r'^$',views.login_view,name='login'),
    url(r'^profile/$',views.display_profile, name='display'),
    url(r'^profile/reset/$',views.reset, name='reset'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^profile/update/$',views.update,name='update'),
    url(r'^profile/about/$',views.hobbies_interests,name='hobbies_interests'),
    url(r'^profile/about/(?P<id>\d+)/$',views.about,name='about'),
    url(r'^roommate/$',views.roommate,name='roommate'),
    url(r'^roommate/choose/$',views.choose_roommate,name='choose_roommate'),
    url(r'^roommate/choose/(?P<stud>\w+)/$',views.select,name='select'),
    url(r'^roommate/custom/$',views.custom_roommate,name='custom_roommate'),
]