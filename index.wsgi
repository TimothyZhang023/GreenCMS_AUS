import os 
import django.core.handlers.wsgi

import sae

os.environ['DJANGO_SETTINGS_MODULE'] = 'web2.settings' # mysite�滻Ϊ���Ӧ����

application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())