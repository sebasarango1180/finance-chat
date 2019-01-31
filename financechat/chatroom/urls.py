from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^room/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
