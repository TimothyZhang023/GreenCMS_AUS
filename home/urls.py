__author__ = 'TianShuo'
from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
                       url(r'^jump', 'jump', name='jump'),

                       url(r'^$', 'manage_index', name='manage_index'),
                       url(r'^index/$', 'manage_index', name='manage_index'),
                       url(r'^version/list$', 'manage_version_list', name='manage_version_list'),
                       url(r'^version/add$', 'manage_version_add', name='manage_version_add'),
                       url(r'^version/del/(?P<id>\d+)/', 'manage_version_del', name='manage_version_del'),
                       url(r'^version/file/$', 'manage_version_file', name='manage_version_file'),
                       url(r'^dashboard/$', 'manage_dashboard', name='manage_dashboard'),
                       url(r'^changepass/$', 'manage_changepass', name='manage_changepass'),

                       url(r'^gcs/upgrade/list$', 'gcs_upgrade_list', name='gcs_upgrade_list'),
                       url(r'^gcs/upgrade/list/old$', 'gcs_upgrade_list_old', name='gcs_upgrade_list_old'),
                       url(r'^gcs/upgrade/add$', 'gcs_upgrade_add', name='gcs_upgrade_add'),
                       url(r'^gcs/upgrade/addHandle$', 'gcs_upgrade_add_handle', name='gcs_upgrade_add_handle'),
                       url(r'^gcs/upgrade/edit/(?P<id>\d+)/', 'gcs_upgrade_edit', name='gcs_upgrade_edit'),
                       url(r'^gcs/upgrade/editHandle/(?P<id>\d+)/', 'gcs_upgrade_edit_handle',
                           name='gcs_upgrade_edit_handle'),
                       url(r'^gcs/upgrade/del/(?P<id>\d+)/', 'gcs_upgrade_del_handle', name='gcs_upgrade_del_handle'),
                       url(r'^gcs/upgrade/restore/(?P<id>\d+)/', 'gcs_upgrade_restore_handle',
                           name='gcs_upgrade_restore_handle'),


                       url(r'^gcs/theme/list$', 'gcs_theme_list', name='gcs_theme_list'),
                       url(r'^gcs/theme/list/old$', 'gcs_theme_list_old', name='gcs_theme_list_old'),

                       url(r'^gcs/theme/add$', 'gcs_theme_add', name='gcs_theme_add'),
                       url(r'^gcs/theme/addHandle$', 'gcs_theme_add_handle', name='gcs_theme_add_handle'),
                       url(r'^gcs/theme/del/(?P<id>\d+)/', 'gcs_theme_del_handle', name='gcs_theme_del_handle'),
                       url(r'^gcs/theme/restore/(?P<id>\d+)/', 'gcs_theme_restore_handle',
                           name='gcs_theme_restore_handle'),


                       url(r'^gcs/plugin/list$', 'gcs_plugin_list', name='gcs_plugin_list'),
                       url(r'^gcs/plugin/list/old$', 'gcs_plugin_list_old', name='gcs_plugin_list_old'),

                       url(r'^gcs/plugin/add$', 'gcs_plugin_add', name='gcs_plugin_add'),
                       url(r'^gcs/plugin/addHandle$', 'gcs_plugin_add_handle', name='gcs_plugin_add_handle'),
                       url(r'^gcs/plugin/del/(?P<id>\d+)/', 'gcs_plugin_del_handle', name='gcs_plugin_del_handle'),
                       url(r'^gcs/plugin/restore/(?P<id>\d+)/', 'gcs_plugin_restore_handle',
                           name='gcs_plugin_restore_handle'),


                       url(r'^gcs/full/list$', 'gcs_full_list', name='gcs_full_list'),


)
