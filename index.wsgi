import os 
import django.core.handlers.wsgi

import sae

os.environ['DJANGO_SETTINGS_MODULE'] = 'web2.settings' # mysite替换为你的应用名

application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())