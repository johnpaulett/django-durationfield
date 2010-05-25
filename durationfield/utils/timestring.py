# -*- coding: utf-8 -*-
"""
Utility functions to convert back and forth between a timestring and timedelta.
"""

from datetime import timedelta

def str_to_timedelta(td_str):
    """
    Returns a timedelta parsed from the native string output of a timedelta.

    Timedelta displays in the format ``X day(s), H:MM:SS.ffffff``
    Both the days section and the microseconds section are optional and ``days``
    is singular in cases where there is only one day.
    """
    if td_str == '':
        return None

    days_str = '0 days'
    if td_str.find('day') != -1:
        # Has a days value
        days_str, td_str = td_str.split(',')

    day_num, _ = days_str.split()
    days = int(day_num)

    us_str = '0'
    if td_str.find('.') != -1:
        # Has microseconds
        td_str, us_str = td_str.split('.')

    microseconds = int(us_str)

    hours_str, minutes_str, seconds_str = td_str.split(':')

    hours = int(hours_str)
    minutes = int(minutes_str)
    seconds = int(seconds_str)

    return timedelta(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds)
