from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^college/(?P<id>[0-9]+)/$', views.collegeView, name="college"),
    url(r'^college/(?P<id>[0-9]+)/academics/$', views.academicsView, name="academics"),
]
