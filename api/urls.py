__author__ = 'TianShuo'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
                       #for old version before greencms v2.5
                       url(r'^update/(?P<version>\d{8})/', 'version', name='version'),  #\d{8,8}/(?P<version>\d{8})

                       #for new version after greencms v2.5
                       url(r'^update/product/gcs/diff/(?P<version>\d{8})/', 'query_gcs_diff', name='query_gcs_diff'),
                       url(r'^update/product/gcs/plugin/(?P<name>(.*))/diff/(?P<version>\d{8})/',
                           'query_gcs_plugin_diff', name='query_gcs_plugin_diff'),
                       url(r'^update/product/gcs/theme/(?P<name>(.*))/diff/(?P<version>\d{8})/',
                           'query_gcs_theme_diff', name='query_gcs_theme_diff'),


)
