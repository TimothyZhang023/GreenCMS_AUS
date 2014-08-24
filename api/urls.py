__author__ = 'TianShuo'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
      url(r'^update/(?P<version>\d{8})/', 'version', name='version'),#\d{8,8}/(?P<version>\d{8})

)
