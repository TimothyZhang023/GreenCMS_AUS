from django.conf.urls import patterns, include, url
from web2 import settings
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('web2.views',
                       url(r'^$', 'index', name='manage_index'),
                       url(r'^api/', include('api.urls')),
                       url(r'^manage/', include('home.urls')),
                       url(r'^auth/', include('auth.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^gcs/', include('api.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
