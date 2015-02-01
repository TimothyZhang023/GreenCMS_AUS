# coding=utf-8
import time
import string

from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.validators import RegexValidator
from django.db.models import Max
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from api.models import Version, GcsVersion, GcsPlugin, GcsTheme
from home.models import Opinion
from web2 import conf, settings
from home.form import UploadFileForm, ChangepwdForm










#
fs = FileSystemStorage(location=settings.UPGRADE_URL)

numeric = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')


@login_required(login_url='auth_login')
def manage_dashboard(request):
    return render_to_response('manage/dashboard.html', {},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def manage_index(request):
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
        import sae.storage

        access_key = sae.const.ACCESS_KEY
        secret_key = sae.const.SECRET_KEY
        appname = sae.const.APP_NAME
        domain_name = "update"  #刚申请的domain

        s = sae.storage.Client()
        ob = sae.storage.Object(f.read())
        url = s.put(domain_name, 'update/' + filename, ob)
        return url


@login_required(login_url='auth_login')
def manage_changepass(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('manage/change_pass.html', RequestContext(request, {'form': form, }))

    elif request.method == 'POST':
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get_opinion('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get_opinion('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('manage/change_pass.html',
                                          RequestContext(request, {'changepwd_success': True, 'form': form}))
            else:
                return render_to_response('manage/change_pass.html',
                                          RequestContext(request, {'form': form, 'oldpassword_is_wrong': True}))
        else:
            return render_to_response('manage/change_pass.html', RequestContext(request, {'form': form, }))


@login_required(login_url='auth_login')
def gcs_upgrade_list(request):
    version_list = GcsVersion.objects.filter(statue=1).order_by('-version').all()
    return render_to_response('manage/gcs_upgrade_list.html', {'version_list': version_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_upgrade_list_old(request):
    version_list = GcsVersion.objects.filter(statue=5).order_by('-version').all()
    return render_to_response('manage/gcs_upgrade_list_old.html', {'version_list': version_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_upgrade_add(request):
    form = UploadFileForm()
    default_version = Opinion.get_opinion('default_version').opinion_value

    lastest_build = str(GcsVersion.objects.all().aggregate(Max('build_target'))['build_target__max'])
    build_target = str(time.strftime('%Y%m%d', time.localtime(time.time())))

    lastest_version = default_version + "." + lastest_build[-4:]
    version_target = default_version + "." + build_target[-4:]

    return render_to_response('manage/gcs_upgrade_add.html',
                              {
                                  'build_from': lastest_build,
                                  'build_target': build_target,
                                  'version_from': lastest_version,
                                  'version_target': version_target,
                                  'form': form
                              },
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_upgrade_edit(request, id=0):
    current_version = GcsVersion.objects.filter(id=id).all()[0]

    lastest_build = current_version.build_from
    build_target = current_version.build_target
    lastest_version = current_version.version_from
    version_target = current_version.version_target
    git_hash = current_version.git_hash
    more_url = current_version.more_url
    description = current_version.description

    form = UploadFileForm()

    return render_to_response('manage/gcs_upgrade_edit.html', {
        'build_from': lastest_build,
        'build_target': build_target,
        'version_from': lastest_version,
        'version_target': version_target,
        'git_hash': git_hash,
        'more_url': more_url,
        'description': description,
        'form': form,
        'version': current_version,
    }, context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_upgrade_add_handle(request):
    if request.method == 'POST':
        print request.POST
        print request._files
        build_target = request.POST['build_target']
        build_from = request.POST['build_from']
        version_from = request.POST['version_from']
        version_target = request.POST['version_target']
        git_hash = request.POST['git_hash']
        more_url = request.POST['more_url']
        description = request.POST['description']
        if not (build_from and build_target and version_from and version_target):
            return HttpResponse("the information is not complete")
            #filename:GreenCMS_20140321_to_20140322.zip
        filename = 'GreenCMS_' + build_from + '_to_' + build_target + '.zip'


        #todo upload file
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], filename)
            version1 = GcsVersion(
                build=build_target,
                version=version_target,
                build_target=build_target,
                build_from=build_from,
                version_target=version_target,
                version_from=version_from,
                statue=1,
                file_name=filename,
                md5_hash="md5",
                git_hash=git_hash,
                more_url=more_url,
                description=description,
                file_server=conf.storage_url,
            )
            version1.save()
            return HttpResponseRedirect(reverse('gcs_upgrade_list'))
        else:
            return HttpResponse("the upload file process occur error")


def gcs_upgrade_edit_handle(request, id=0):
    if id == 0:
        raise Http404()

    build_target = request.POST['build_target']
    build_from = request.POST['build_from']
    version_from = request.POST['version_from']
    version_target = request.POST['version_target']
    git_hash = request.POST['git_hash']
    more_url = request.POST['more_url']
    description = request.POST['description']

    version = GcsVersion.objects.get(id=id)
    version.build_target = build_target
    version.build_from = build_from
    version.version_from = version_from
    version.version_target = version_target
    version.git_hash = git_hash
    version.more_url = more_url
    version.description = description
    version.file_server = conf.storage_url

    version.save()

    return HttpResponseRedirect(reverse('gcs_upgrade_list'))


@login_required(login_url='auth_login')
def gcs_upgrade_del_handle(request, id=0):
    if id == 0:
        raise Http404()

    version = GcsVersion.objects.get(id=id)
    version.statue = 5
    version.save()

    return HttpResponseRedirect(reverse('gcs_upgrade_list'))


@login_required(login_url='auth_login')
def gcs_upgrade_restore_handle(request, id=0):
    if id == 0:
        raise Http404()

    version = GcsVersion.objects.get(id=id)
    version.statue = 1
    version.save()

    return HttpResponseRedirect(reverse('gcs_upgrade_list'))


@login_required(login_url='auth_login')
def gcs_theme_list(request):
    theme_list = GcsTheme.objects.filter(statue=1).order_by('-build').all()

    return render_to_response('manage/gcs_theme_list.html', {'theme_list': theme_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_plugin_list(request):
    plugin_list = GcsPlugin.objects.filter(statue=1).order_by('-build').all()

    return render_to_response('manage/gcs_plugin_list.html', {'plugin_list': plugin_list},
                              context_instance=RequestContext(request))

@login_required(login_url='auth_login')
def gcs_theme_list_old(request):
    theme_list = GcsTheme.objects.filter(statue=5).order_by('-build').all()

    return render_to_response('manage/gcs_theme_list_old.html', {'theme_list': theme_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_plugin_list_old(request):
    plugin_list = GcsPlugin.objects.filter(statue=5).order_by('-build').all()

    return render_to_response('manage/gcs_plugin_list_old.html', {'plugin_list': plugin_list},
                              context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_full_list(request):
    return render_to_response('manage/gcs_full_list.html')


@login_required(login_url='auth_login')
def jump(request):
    destination = request.GET.get_opinion('des', '')
    return render_to_response('jump.html', {'destination': destination}, context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_theme_add_handle(request):
    if request.method == 'POST':
        print request.POST
        print request._files
        theme_name = request.POST['theme_name']
        build = request.POST['build']
        version = request.POST['version']

        author = request.POST['author']
        more_url = request.POST['more_url']
        description = request.POST['description']

        if not (theme_name and build and version and author):
            return HttpResponse("the information is not complete")

            #filename:GCS_Theme-NovaGreenStudio_build_
        filename = 'GCS_Theme-' + theme_name + '_build_' + build + '.zip'


        #todo upload file
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], filename)
            theme1 = GcsTheme(
                theme_name=theme_name,

                build=build,
                version=version,
                author=author,
                statue=1,
                md5_hash="md5",

                more_url=more_url,
                description=description,

                file_name=filename,
                file_server=conf.storage_url,
            )
            theme1.save()
            return HttpResponseRedirect(reverse('gcs_theme_list'))
        else:
            return HttpResponse("the upload file process occur error")


@login_required(login_url='auth_login')
def gcs_plugin_add_handle(request):
    if request.method == 'POST':
        print request.POST
        print request._files
        plugin_name = request.POST['plugin_name']
        build = request.POST['build']
        version = request.POST['version']

        author = request.POST['author']
        more_url = request.POST['more_url']
        description = request.POST['description']

        if not (plugin_name and build and version and author):
            return HttpResponse("the information is not complete")

            #filename:GCS_Plugin-Weather_build_
        filename = 'GCS_Theme-' + plugin_name + '_build_' + build + '.zip'


        #todo upload file
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], filename)
            plugin1 = GcsPlugin(
                plugin_name=plugin_name,

                build=build,
                version=version,
                author=author,
                statue=1,
                md5_hash="md5",

                more_url=more_url,
                description=description,

                file_name=filename,
                file_server=conf.storage_url,
            )
            plugin1.save()
            return HttpResponseRedirect(reverse('gcs_plugin_list'))
        else:
            return HttpResponse("the upload file process occur error")


@login_required(login_url='auth_login')
def gcs_theme_add(request):
    form = UploadFileForm()

    return render_to_response('manage/gcs_theme_add.html', {'form': form}, context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_plugin_add(request):
    form = UploadFileForm()

    return render_to_response('manage/gcs_plugin_add.html', {'form': form}, context_instance=RequestContext(request))


@login_required(login_url='auth_login')
def gcs_theme_del_handle(request, id):
    if id == 0:
        raise Http404()

    theme = GcsTheme.objects.get(id=id)
    theme.statue = 5
    theme.save()

    return HttpResponseRedirect(reverse('gcs_theme_list'))


@login_required(login_url='auth_login')
def gcs_theme_restore_handle(request, id):
    if id == 0:
        raise Http404()

    theme = GcsTheme.objects.get(id=id)
    theme.statue = 1
    theme.save()

    return HttpResponseRedirect(reverse('gcs_theme_list_old'))


@login_required(login_url='auth_login')
def gcs_plugin_del_handle(request, id):
    if id == 0:
        raise Http404()

    plugin = GcsPlugin.objects.get(id=id)
    plugin.statue = 5
    plugin.save()

    return HttpResponseRedirect(reverse('gcs_plugin_list'))


@login_required(login_url='auth_login')
def gcs_plugin_restore_handle(request, id):
    if id == 0:
        raise Http404()

    plugin = GcsPlugin.objects.get(id=id)
    plugin.statue = 1
    plugin.save()

    return HttpResponseRedirect(reverse('gcs_plugin_list_old'))
