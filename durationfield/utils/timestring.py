# -*- coding: utf-8 -*-
"""
Utility functions to convert back and forth between a timestring and timedelta.
  1y 7m 6w 3d 18h 30min 23s 10ms 150us
    => 1 year 7 months 6 weeks 3 days 18 hours 30 minutes 23 seconds 1 milliseconds 150 microseconds
    => datetime.timedelta(624, 6155, 805126)
"""

from datetime import timedelta
from django.utils.datastructures import SortedDict

values_in_microseconds = SortedDict((
    # Uncomment the following two lines for year and month support
    # ('y', 31556925993600), # 52.177457 * (7*24*60*60*1000*1000)
    # ('m', 2629743832800), # 4.34812141 * (7*24*60*60*1000*1000)
    ('w', 604800000000), # 7*24*60*60*1000*1000
    ('d', 86400000000), # 24*60*60*1000*1000
    ('h', 3600000000), # 60*60*1000*1000
    ('min', 60000000), # 60*1000*1000
    ('s',  1000000), # 1000*1000
    ('ms', 1000),
    ('us', 1),
))

def to_timedelta(value):
    chunks = []
    for b in value.lower().split():
        for index, char in enumerate(b):
            if not char.isdigit():
                chunks.append((b[:index], b[index:])) # digits, letters
                break

    microseconds = 0
    for digits, chars in chunks:
        if not digits or not chars in values_in_microseconds:
            raise ValueError('Incorrect timestring pair')
        microseconds += int(digits) * values_in_microseconds[chars]

    return timedelta(microseconds=microseconds)

def from_timedelta(value):
    if not value:
        return u'0s'

    if not isinstance(value, timedelta):
        raise ValueError('to_timestring argument must be a datetime.timedelta instance')

    chunks = []
    microseconds = value.days * 24 * 3600 * 1000000 + value.seconds * 1000000 + value.microseconds
    for k in values_in_microseconds:
        if microseconds >= values_in_microseconds[k]:
            diff, microseconds = divmod(microseconds, values_in_microseconds[k])
            chunks.append('%d%s' % (diff, k))
    return u' '.join(chunks)
