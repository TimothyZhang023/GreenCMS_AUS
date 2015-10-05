__author__ = 'TianShuo'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
                       url(r'^index/$', 'manage_index', name='manage_index'),
                       url(r'^version/list$', 'manage_version_list', name='manage_version_list'),
                       url(r'^version/add$', 'manage_version_add', name='manage_version_add'),
                       url(r'^version/del/(?P<id>\d+)/', 'manage_version_del', name='manage_version_del'),
                       url(r'^version/file', 'manage_version_file', name='manage_version_file'),
                       url(r'^dashboard/$', 'manage_dashboard', name='manage_dashboard'),
)
