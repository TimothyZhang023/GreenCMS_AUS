# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.validators import RegexValidator
from api.models import Version
from web2 import conf, settings
from django.db.models import Max
from django.http import Http404, HttpResponse, StreamingHttpResponse,HttpResponseRedirect
import string
from home.form import UploadFileForm
from django.core.files.storage import FileSystemStorage
#
fs = FileSystemStorage(location=settings.UPGRADE_URL)

# Create your views here.
numeric = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')


@login_required(login_url='auth_login')
def manage_dashboard(request):
    return render_to_response('manage/dashboard.html', {},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def manage_index(request):
    #return HttpResponse("manage_index")
    return HttpResponseRedirect(reverse('manage_dashboard'))



@login_required(login_url='auth_login')
def manage_version_list(request):
    version_list = Version.objects.order_by('-version').all()
    return render_to_response('manage/version_list.html', {'version_list': version_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def manage_version_add(request):
    if request.method == 'GET':
        form = UploadFileForm()
        lastest_version = Version.objects.all().aggregate(Max('version'))
        build_from = string.atoi(lastest_version["version__max"])
        return render_to_response('manage/version_add.html', {'build_from': build_from, 'form': form},
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        print request.POST
        print request._files
        build_to = request.POST['build_to']
        build_from = request.POST['build_from']
        version_to = request.POST['version_to']
        git_hash = request.POST['git_hash']
        if not (build_to and build_to and version_to and git_hash):
            return HttpResponse("信息不全")
            #filename:GreenCMS_20140321_to_20140322.zip
        filename = 'GreenCMS_' + build_from + '_to_' + build_to + '.zip'
        #todo check if where has this version

        #todo upload file
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], filename)
            version1 = Version(version=build_to, build_to=build_to, build_from=build_from,
                               version_to=version_to, filename=filename, git_hash=git_hash)
            version1.save()
            return HttpResponseRedirect(reverse('manage_version_list'))
        else:
            return HttpResponse("error")


@login_required(login_url='auth_login')
def manage_version_del(request, id=0):
    if id == 0:
        raise Http404()

    version = Version.objects.get(id=id)
    version.delete()

    return HttpResponseRedirect(reverse('manage_version_list'))


@login_required(login_url='auth_login')
def manage_version_file(request):
    return HttpResponse("manage_version_file")


def handle_uploaded_file(f, filename):
    if settings.not_sae:
        with fs._open(filename, 'wb+') as info:
            for chunk in f.chunks():
                info.write(chunk)
        return f

    else:
        #on sae
        import sae.const

        access_key = sae.const.ACCESS_KEY
        secret_key = sae.const.SECRET_KEY
        appname = sae.const.APP_NAME
        domain_name = "update"  #刚申请的domain

        import sae.storage

        s = sae.storage.Client()
        ob = sae.storage.Object(f.read())
        url = s.put(domain_name, 'update/' + filename, ob)
        return url