import os
from django.core.wsgi import get_wsgi_application

#os.environ['DJANGO_SETTINGS_MODULE'] = 'metashare.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metashare.settings')
application = get_wsgi_application()
