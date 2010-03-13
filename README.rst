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


Althought written to support Django 1.2, experimental Django 1.1 support has 
been added. 

This is beta software, please test thouroughly before putting into production
and report back any issues.
 
Years and Months
----------------

You will need to uncomment two lines in timestring.py to support years and months.


Usage
-----

In models.py::

    from durationfield.db.models.fields.duration import DurationField

    class Time(models.Model):
        ...
        duration = models.DurationField()
        ...


Example
-------

Enter the time into the textbox in the following format::
    
    1y 7m 6w 3d 18h 30min 23s 10ms 150us

This is interpreted as::
    
    1 year 7 months 6 weeks 3 days 18 hours 30 minutes 23 seconds 1 milliseconds 150 microseconds

In your application it will be represented as a python datetime::
    
    datetime.timedelta(624, 6155, 805126)

This will be stored into the database as a 'bigint' with the value of::
    
    53919755833350


