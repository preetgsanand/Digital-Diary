from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.create),
    url(r'^list/$', views.list),
    url(r'^list/(?P<id>\d+)/$',views.detail,name="detail"),
]
