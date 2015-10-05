from django.conf.urls import patterns, include, url
from web2 import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^api/', include('api.urls')),
                       url(r'^manage/', include('home.urls')),
                       url(r'^auth/', include('auth.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^docs/', include('docs.urls')),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
