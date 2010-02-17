from distutils.core import setup

import durationfield
packages = ['durationfield',
            'durationfield.db',
            'durationfield.db.models',
            'durationfield.db.models.fields',
            'durationfield.forms',
            'durationfield.utils']
setup(
    name = 'django-durationfield',
    version = durationfield.__version__,
    packages = packages,
    maintainer = 'John Paulett',
    maintainer_email = 'john@paulett.org',
    description = durationfield.__doc__,
    keywords = 'django',
    url = 'http://github.com/johnpaulett/django-durationfield/',
)
