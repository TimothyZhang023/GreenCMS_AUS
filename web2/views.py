__author__ = 'TianShuo'
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponseRedirect(reverse('manage_dashboard'))

