from django.contrib import admin
from api.models import Version
# Register your models here.


class Version_admin(admin.ModelAdmin):
    list_display = ('version', 'build_to', 'build_from', 'filename', 'version_to', 'git_hash')
    list_filter = ('version', 'build_to', 'build_from')
    #readonly_fields = ('user',)
    search_fields = ['version', 'build_to', 'build_from']


admin.site.register(Version, Version_admin)
