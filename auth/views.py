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
    redirect_to = request.REQUEST.get('next', '/manage/dashboard/')

    if request.method == 'GET':
        return render_to_response('manage/login.html',
                                  {'conf': conf, 'title': u'GreenCMS Active Update System', 'redirect_to': redirect_to},
                                  context_instance=RequestContext(request))

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Login Error. Please, check your username and password')
        login(request, user)
        request.session['username'] = user.username
        request.session['email'] = user.email

        return HttpResponseRedirect(redirect_to)
    else:
        return HttpResponse("error")


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_login'))

