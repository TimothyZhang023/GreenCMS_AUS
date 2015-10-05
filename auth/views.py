# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from web2 import conf
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def auth_login(request):
    if request.method == 'GET':
        return render_to_response('manage/login.html',
                                  {'conf': conf, 'title': u'登录GreenCMS API管理系统'},
                                  context_instance=RequestContext(request))

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('登陆失败，请检查用户名密码是否错误')
        login(request, user)
        request.session['username'] = user.username
        request.session['email'] = user.email

        return HttpResponseRedirect(reverse('manage_index'))
    else:
        return HttpResponse("error")


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_login'))

@login_required(login_url='auth_login')
def auth_changepass(request):
    return HttpResponse("auth_changepass")