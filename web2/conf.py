#encoding=utf-8
from web2 import settings
import os
from os import environ

site_name = u'GreenCMS API'

debug = not environ.get("APP_NAME", "")
if debug:
    site_url = r'http://127.0.0.1:8000'
    storage_url = r'http://127.0.0.1:8000/static/upgrade/'
else:
#SAE
    site_url = r'http://greenapi.sinaapp.com'
    storage_url = r'http://greenapi-update.stor.sinaapp.com/update/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_PATH = os.path.join(BASE_DIR, 'static/upload')
UPGRADE_PATH = os.path.join(BASE_DIR, 'static/upgrade')
