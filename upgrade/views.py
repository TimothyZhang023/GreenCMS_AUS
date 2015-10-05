import json
import string
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
from django.db.models import Max
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from common.models import Version, GcsVersion, GcsPlugin, GcsTheme
from greencms_aus import settings

upload_storage = FileSystemStorage(
    location=settings.UPLOAD_PATH,
    base_url=settings.SITE_URL + '/static/upload/'
)

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', 'Only alphanumeric characters and underscore are allowed.')


@csrf_exempt
def version(request, version=0):
    """
    GreenCMS Old version upgrade API
    :param request:
    :param version:
    :return: json result
    """
    if version == 0:
        raise Http404()

    user_version = string.atoi(version)

    lastest_version = Version.objects.all().aggregate(Max('version'))

    version_check_res = {}
    file_list = {}
    # .filter(version__gt=user_version)
    for versions in Version.objects.filter(version__gt=user_version).all():
        version_temp = {
            'version': versions.version,
            'file_name': versions.filename,
            'file_url': settings.STORAGE_URL + versions.filename,
            'build_from': versions.build_from,
            'build_to': versions.build_to,
            'git_hash': versions.git_hash,
            'version_to': versions.version_to
        }

        file_list[versions.version] = version_temp

    version_check_res['user_version'] = user_version
    version_check_res['lastest_version'] = string.atoi(lastest_version["version__max"])
    version_check_res['file_list'] = file_list

    return HttpResponse(json.dumps(version_check_res), content_type="application/json")


@csrf_exempt
def query_gcs_diff(request, version):
    if version == 0:
        raise Http404()
    user_build = string.atoi(version)
    lastest_build = GcsVersion.objects.filter(statue=1).all().aggregate(Max('build'))

    version_check_res = {}
    file_list = {}
    # .filter(version__gt=user_build)
    for versionItem in GcsVersion.objects.filter(version__gt=user_build, statue=1).all():
        version_temp = {'version': versionItem.version,
                        'file_name': versionItem.file_name,
                        'file_url': settings.STORAGE_URL + versionItem.file_name,

                        'build_from': versionItem.build_from,
                        'build_target': versionItem.build_target,

                        'version_from': versionItem.version_from,
                        'version_target': versionItem.version_target,

                        'git_hash': versionItem.git_hash,
                        'md5_hash': versionItem.md5_hash,
                        'description': versionItem.description,
                        'file_server': versionItem.file_server,
                        }

        file_list[versionItem.version] = version_temp

    version_check_res['user_build'] = user_build
    version_check_res['latest_build'] = lastest_build["build__max"]
    version_check_res['diff_list'] = file_list

    return HttpResponse(json.dumps(version_check_res), content_type="application/json")


def query_gcs_plugin_diff(request, name, version):
    return HttpResponse("query_gcs_plugin_diff" + name + version)
    pass


def query_gcs_theme_diff(request, name, version):
    return HttpResponse("query_gcs_theme_diff" + name + version)
    pass


def query_gcs_plugin_list(request):
    plugin_list_db = GcsPlugin.objects.filter(statue=1).all()
    plugin_list = {}
    file_list = {}

    for pluginItem in plugin_list_db:
        version_temp = {
            'version': pluginItem.version,
            'build': pluginItem.build,
            'plugin_name': pluginItem.plugin_name,

            'file_name': pluginItem.file_name,
            'file_server': pluginItem.file_server,
            'file_url': settings.STORAGE_URL + pluginItem.file_name,

            'author': pluginItem.author,
            'submit_date': pluginItem.submit_date.strftime('%Y-%m-%d'),

            'description': pluginItem.description,
            'more_url': pluginItem.more_url,

            'md5_hash': pluginItem.md5_hash,
        }
        file_list[pluginItem.plugin_name] = version_temp

    plugin_list['list'] = file_list

    return HttpResponse(json.dumps(plugin_list), content_type="application/json")


def query_gcs_theme_list(request):
    theme_list_db = GcsTheme.objects.filter(statue=1).all()
    theme_list = {}
    file_list = {}

    for themeItem in theme_list_db:
        version_temp = {
            'version': themeItem.version,
            'build': themeItem.build,
            'theme_name': themeItem.theme_name,

            'file_name': themeItem.file_name,
            'file_server': themeItem.file_server,
            'file_url': settings.STORAGE_URL + themeItem.file_name,

            'author': themeItem.author,
            'submit_date': themeItem.submit_date.strftime('%Y-%m-%d'),

            'description': themeItem.description,
            'more_url': themeItem.more_url,

            'md5_hash': themeItem.md5_hash,
        }
        file_list[themeItem.plugin_name] = version_temp

    theme_list['list'] = file_list

    return HttpResponse(json.dumps(theme_list), content_type="application/json")


def query_gcs_plugin_detail(request, name):
    pass


def query_gcs_theme_detail(request, name):
    pass
