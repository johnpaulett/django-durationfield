# -*- coding: utf-8 -*-
"""Temporary reusable application for a DurationField in Django.

The django-durationfield package is a temporary solution for `#2443 <http://code.djangoproject.com/ticket/2443>`_,
"Add IntervalField to database models." Since the existing patch was not
committed before the 1.2 feature deadline, this package attempts to make the
patch into a reusable application that provides a ``DurationField``.

This package will aim to stay in sync with the latest patch attached to the
ticket and to make the (hopefully) eventual migration of DurationField into
Django core as simple as switching a few import statements.  My current plan
is that django-durationfield will be deprecated as soon as #2443 is merged
into the Django trunk.

I thank the authors of the original DurationField patches, Marty Alchin, Adys,
and Yuri Baburov.

The code in this app is currently based on the 2010-01-25 patch by Adys,
`DurationField.patch <http://code.djangoproject.com/attachment/ticket/2443/durationfield.patch>`_

Usage:
TODO
"""
__version__ = '0.1'
