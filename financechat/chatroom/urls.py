from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='chatroom'),
    url(r'^room/(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'register/$', views.register, name='register'),
    url(r'profile/$', views.show_profile, name='profile')
]
