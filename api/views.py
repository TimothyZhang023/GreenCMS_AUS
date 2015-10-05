from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.validators import RegexValidator
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.core import serializers
import json
import string
from django.views.decorators.csrf import csrf_exempt

from api.models import Version
from web2 import conf
from django.db.models import Max

upload_storage = FileSystemStorage(
    location=conf.UPLOAD_PATH,
    base_url=conf.site_url + '/static/upload/'
)

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', 'Only alphanumeric characters and underscore are allowed.')


@csrf_exempt
def version(request, version=0):
    if version == 0:
        raise Http404()

    user_version = string.atoi(version)

    lastest_version = Version.objects.all().aggregate(Max('version'))

    version_check_res = {}
    file_list = {}
    #.filter(version__gt=user_version)
    for versions in Version.objects.filter(version__gt=user_version).all():
        version_temp = {};
        version_temp['version'] = versions.version
        version_temp['file_name'] = versions.filename
        version_temp['file_url'] = conf.storage_url + versions.filename
        version_temp['build_from'] = versions.build_from
        version_temp['build_to'] = versions.build_to
        version_temp['git_hash'] = versions.git_hash
        version_temp['version_to'] = versions.version_to

        file_list[versions.version] = version_temp

    version_check_res['user_version'] = user_version
    version_check_res['lastest_version'] = string.atoi(lastest_version["version__max"])
    version_check_res['file_list'] = file_list

    return HttpResponse(json.dumps(version_check_res), content_type="application/json")

    #return HttpResponse(json.dumps(version_check_res, ensure_ascii=False))
