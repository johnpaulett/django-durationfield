from distutils.core import setup

import durationfield

setup(
    name = 'django-durationfield',
    version = durationfield.__version__,
    packages = ['durationfield'],
    maintainer = 'John Paulett',
    maintainer_email = 'john@paulett.org',
    description = durationfield.__doc__,
    keywords = 'django',
    url = 'http://github.com/johnpaulett/django-durationfield/',
)
