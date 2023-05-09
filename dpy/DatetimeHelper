"""
.. module:: DatetimeHelper
   :synopsis: Classes & Utilities related to datetime
   
Module: DatetimeHelper

Define classes & Utilities related to datetime
"""
import datetime

def last_day_of_month(any_day: datetime.datetime):
    """
    Return the last date of the month of the given date
    """
    # The day 27 exists in every month. 10 days later, it's always next month
    next_month = any_day.replace(day=27) + datetime.timedelta(days=10)
    # subtracting the number of the current day brings us back one month
    return next_month - datetime.timedelta(days=next_month.day)

def last_day_of_week(dt: datetime.datetime):
    """
    Return the last date of the week of the given date
    """
    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=4)
    return end
