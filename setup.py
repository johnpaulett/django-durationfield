from distutils.core import setup

import durationfield
packages = ['durationfield',
            'durationfield.db',
            'durationfield.db.models',
            'durationfield.db.models.fields',
            'durationfield.forms',
            'durationfield.utils']
setup(
    name='django-durationfield',
    version=durationfield.__version__,
    packages=packages,
    maintainer='John Paulett',
    maintainer_email='john@paulett.org',
    description='Reusable app for adding a DurationField to Django',
    long_description=durationfield.__doc__,
    keywords=['django', 'duration field', 'interval field'],
    url='https://django-durationfield.readthedocs.org',
    license='BSD',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
