# -*- coding: utf-8 -*-
"""
Utility functions to convert back and forth between a timestring and timedelta.
"""

from django.conf import settings

from datetime import timedelta
import re

ALLOW_MONTHS = getattr(settings, "DURATIONFIELD_ALLOW_MONTHS", False)
ALLOW_YEARS = getattr(settings, "DURATIONFIELD_ALLOW_YEARS", False)
MONTHS_TO_DAYS = getattr(settings, "DURATIONFIELD_MONTHS_TO_DAYS", 30)
YEARS_TO_DAYS = getattr(settings, "DURATIONFIELD_YEARS_TO_DAYS", 365)

def str_to_timedelta(td_str):
    """
    Returns a timedelta parsed from the native string output of a timedelta.

    Timedelta displays in the format ``X day(s), H:MM:SS.ffffff``
    Both the days section and the microseconds section are optional and ``days``
    is singular in cases where there is only one day.

    Additionally will handle user input in months and years, translating those
    bits into a count of days which is 'close enough'.
    """
    time_format = r"(?:(?P<days>\d+)\W*(?:days?|d),?)?\W*(?:(?P<hours>\d+):(?P<minutes>\d+)(?::(?P<seconds>\d+)(?:\.(?P<microseconds>\d+))?)?)?"
    if ALLOW_MONTHS:
        time_format = r"(?:(?P<months>\d+)\W*(?:months?|m),?)?\W*" + time_format
    if ALLOW_YEARS:
        time_format = r"(?:(?P<years>\d+)\W*(?:years?|y),?)?\W*" + time_format
    time_matcher = re.compile(time_format)
    time_matches = time_matcher.match(td_str)
    time_groups = time_matches.groupdict()

    for key in time_groups.keys():
        if time_groups[key]:
            time_groups[key] = int(time_groups[key])
        else:
            time_groups[key] = 0

    if "years" in time_groups.keys():
        time_groups["days"] = time_groups["days"] + (time_groups["years"] * YEARS_TO_DAYS)
    if "months" in time_groups.keys():
        time_groups["days"] = time_groups["days"] + (time_groups["months"] * MONTHS_TO_DAYS)

    return timedelta(
        days=time_groups["days"],
        hours=time_groups["hours"],
        minutes=time_groups["minutes"],
        seconds=time_groups["seconds"],
        microseconds=time_groups["microseconds"])
