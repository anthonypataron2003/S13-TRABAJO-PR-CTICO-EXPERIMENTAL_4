import os
from pathlib import Path
from .config_product import PRODUCTS
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY','local-demo-only-not-for-production')
DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1']
PRODUCT_VARIANT = os.getenv('PRODUCT_VARIANT','A').upper()
if PRODUCT_VARIANT not in PRODUCTS: raise ValueError('PRODUCT_VARIANT debe ser A o B')
ENABLE_REPORTS = PRODUCTS[PRODUCT_VARIANT]['ENABLE_REPORTS']
ENABLE_NOTIFICATIONS = PRODUCTS[PRODUCT_VARIANT]['ENABLE_NOTIFICATIONS']
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','usuarios','inventario']
if ENABLE_REPORTS: INSTALLED_APPS.append('reportes')
if ENABLE_NOTIFICATIONS: INSTALLED_APPS.append('notificaciones')
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages','usuarios.context.features']}}]
DATABASES = {'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
LANGUAGE_CODE='es'
TIME_ZONE='America/Guayaquil'
USE_I18N=True
USE_TZ=True
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='login'
LOGIN_REDIRECT_URL='dashboard'
LOGOUT_REDIRECT_URL='login'
