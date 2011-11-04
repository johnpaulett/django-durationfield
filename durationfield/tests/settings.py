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
    'durationfield.tests',
)

DURATIONFIELD_ALLOW_YEARS = True
DURATIONFIELD_ALLOW_MONTHS = True
