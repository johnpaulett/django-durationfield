import django

version = django.VERSION[0:3]

if version[0] <= 1 and version[1] < 2:
    # use old syntax for Django<1.2
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = 'durationfieldtest.db'
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'durationfieldtest.db',
            }
        }
  
INSTALLED_APPS = (
    'tests',
)

DURATIONFIELD_ALLOW_YEARS = True
DURATIONFIELD_ALLOW_MONTHS = True

SECRET_KEY = '_2roqfdp42u3qn23xc=z4**vueob2#!yloe=_+go&wxsi&glt1'
