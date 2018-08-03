from django.conf.urls import url
from . import views  


urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^logout$', views.logout),
  url(r'^dashboard$', views.dashboard),
  url(r'^comment$', views.comment),
  url(r'^user_profile/(?P<id>\d+)$', views.user_profile),


]