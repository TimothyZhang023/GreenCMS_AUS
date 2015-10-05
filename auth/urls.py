__author__ = 'TianShuo'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth.views',
                       url(r'^login/$', 'auth_login', name='auth_login'),
                       url(r'^logout/$', 'auth_logout', name='auth_logout'),
                       url(r'^changepass/$', 'auth_changepass', name='auth_changepass'),



)
