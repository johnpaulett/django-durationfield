DurationField
=============

Reusable application for a DurationField in Django.

This reusable app was conceived as a temporary solution for an old request to add
native support for an interval or duration field to Django core, 
`#2443 <http://code.djangoproject.com/ticket/2443>`_,
"Add IntervalField to database models." This app started from the 
2010-01-25 patch by Adys,
`DurationField.patch <http://code.djangoproject.com/attachment/ticket/2443/durationfield.patch>`_ and has evolved considerably as people have used it in their 
own applications.


There have been discussions as to the merit of including into a DurationField
in Django core.  As of the moment, it appears that most developers favor
keeping DurationField separate from Django (both to prevent bloat and to allow
rapid evolution of the DurationField's implementation).

That being said, we have developed the DurationField so that if it ever does
get merged into Django core, it should be simple for users to switch.

This is beta software, please test thoroughly before putting into production
and report back any issues.


Django Versions
---------------

django-duration field has been tested on Django 1.1.4 through Django 1.3.  Please
report any bugs or patches in improve version support.

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

In your application it will be represented as a python ``datetime.timedelta``::
    
    45 days, 18:30:23.010150

This will be stored into the database as a 'bigint' with the value of::
    
    3954623010150

 
Years and Months
----------------

You will need to uncomment two lines in timestring.py to support years and months. This causes a 
loss of precision because the number of days in a month is not exact. This has not been extensively tested.

Testing
-------

If you are interested in developing django-duration field, the following commands
can help you test django-durationfield across all current versions of Django.

Django 1.3::

    virtualenv --no-site-packages env1.3
    source env1.3/bin/activate
    pip install http://www.djangoproject.com/download/1.3-rc-1/tarball/
    cd durationfield/tests
    ./test.sh


Django 1.2::

    virtualenv --no-site-packages env1.2
    source env1.2/bin/activate
    pip install Django==1.2.5
    cd durationfield/tests
    ./test.sh

Django 1.1::

    virtualenv --no-site-packages env1.1
    source env1.1/bin/activate
    pip install Django==1.1.4
    cd durationfield/tests
    ./test.sh


Authors
-------

Thanks to the authors of the original DurationField patches, Marty Alchin, Adys,
and Yuri Baburov.

Thanks to the contributors to django-durationfield:

 * John Paulet (https://github.com/johnpaulett)
 * Paul Oswald (https://github.com/poswald)
 * Wes Winham (https://github.com/winhamwr)
 * Guillaume Libersat (https://github.com/glibersat)
 * Jason Mayfield (https://github.com/jwmayfield)
 * silent1mezzo (https://github.com/silent1mezzo)
