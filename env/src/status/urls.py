from django.conf.urls import url
from status import views

urlpatterns = [
    url(r'^$', views.status_home),
    url(r'^create/$', views.status_create),
    url(r'^update/$', views.status_home),
    url(r'^search/(?P<id>\d+)/$', views.status_search,name="search"),
    url(r'^delete/$', views.status_home),
]
