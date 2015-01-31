__author__ = 'TianShuo'
from django.conf.urls import patterns, url

urlpatterns = patterns('auth.views',
                       url(r'^login/$', 'auth_login', name='auth_login'),
                       url(r'^logout/$', 'auth_logout', name='auth_logout'),

)
