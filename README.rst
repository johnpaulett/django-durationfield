DurationField
=============

Temporary reusable application for a DurationField in Django.

The django-durationfield package is a temporary solution for `#2443 <http://code.djangoproject.com/ticket/2443>`_,
"Add IntervalField to database models." Since the existing patch was not
committed before the 1.2 feature deadline, this package attempts to make the
patch into a reusable application that provides a ``DurationField``.
 
This package will aim to stay in sync with the latest patch attached to the
ticket and to make the (hopefully) eventual migration of DurationField into
Django core as simple as switching a few import statements.  My current plan
is that django-durationfield will be deprecated as soon as #2443 is merged
into the Django trunk.
 
Thanks to the authors of the original DurationField patches, Marty Alchin, Adys,
and Yuri Baburov.

The code in this app is currently based on the 2010-01-25 patch by Adys,
`DurationField.patch <http://code.djangoproject.com/attachment/ticket/2443/durationfield.patch>`_

Django 1.1.X
------------

Althought written to support Django 1.2, experimental Django 1.1 support has 
been added. Please check out the django-1.1.X branch for that.

This is beta software, please test thouroughly before putting into production
and report back any issues.
 
Years and Months
----------------

You will need to uncomment two lines in timestring.py to support years and months. This causes a 
loss of precision because the number of days in a month is not exact. This has not been extensively tested.

Usage
-----

In models.py::

    from durationfield.db.models.fields.duration import DurationField

    class Time(models.Model):
        ...
        duration = DurationField()
        ...

In your forms::

    from durationfield.forms import DurationField as FDurationField
    
    class MyForm(forms.ModelForm):
        duration = FDurationField()

Note that database queries still need to treat the values as integers. If you are using things like 
aggregates, you will need to explicitly convert them to timedeltas yourself:

    timedelta(microseconds=list.aggregate(sum=Sum('duration'))['sum'])

You can also make a template filter to render out duration values. Create a file called duration.py::

    myapp/templatetags/__init__.py
    myapp/templatetags/duration.py

And put this code in it::

    from django import template
    from durationfield.utils.timestring import from_timedelta
    
    register = template.Library()
    
    def duration(value, arg=None):
        if not value:
            return u""
        return u"%s" % from_timedelta(value)
    
    register.filter('duration', duration)
    
Then in your HTML template::


    {% load duration %}    

    ....
    
    <span>{{object.duration|duration}}</span>


Example
-------

Enter the time into the textbox in the following format::
    
    6w 3d 18h 30min 23s 10ms 150us

This is interpreted as::
    
    6 weeks 3 days 18 hours 30 minutes 23 seconds 1 milliseconds 150 microseconds

In your application it will be represented as a python datetime::
    
    45 days, 18:30:23.010150

This will be stored into the database as a 'bigint' with the value of::
    
    3954623010150


