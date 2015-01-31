__author__ = 'TianShuo'
from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',

                       #for old version before greencms v2.5
                       #\d{8,8}/(?P<version>\d{8})
                       url(r'^update/(?P<version>\d{8})/', 'version', name='version'),


                       #for new version after greencms v2.5
                       url(r'^update/product/gcs/diff/(?P<version>\d{8})/', 'query_gcs_diff', name='query_gcs_diff'),
                       url(r'^update/product/gcs/plugin/(?P<name>(.*))/diff/(?P<version>\d{8})/',
                           'query_gcs_plugin_diff', name='query_gcs_plugin_diff'),
                       url(r'^update/product/gcs/theme/(?P<name>(.*))/diff/(?P<version>\d{8})/',
                           'query_gcs_theme_diff', name='query_gcs_theme_diff'),
                       url(r'^update/product/gcs/plugin/list/',
                           'query_gcs_plugin_list', name='query_gcs_plugin_list'),
                       url(r'^update/product/gcs/theme/list/',
                           'query_gcs_theme_list', name='query_gcs_theme_list'),
                       url(r'^update/product/gcs/plugin/(?P<name>(.*))/$',
                           'query_gcs_plugin_detail', name='query_gcs_plugin_detail'),
                       url(r'^update/product/gcs/theme/(?P<name>(.*))/$',
                           'query_gcs_theme_detail', name='query_gcs_theme_detail'),

)
