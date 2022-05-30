from pickle import FALSE
from .base import *
import os



SECRET_KEY = os.environ["DJANGO_SECRETE_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['localhost', 'arabfonts.org', 'www.arabfonts.org']