# calendarapp/utils.py
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import *


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter reserve by day
    def formatday(self, day, reserve):
        reserve_per_day = reserve.filter(dateEntrée__day=day)
        d = ""
        for event in reserve_per_day:
            d += f"<li> {event.administration} </li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, reserve):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, reserve)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    # filter reserve by year and month
    def formatmonth(self, withyear=True):
        reserve =Ressalle.objects.filter(dateEntrée__year=self.year, dateEntrée__month=self.month)
        cal = ('<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n')  # noqa
        cal += (f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n")  # noqa
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, reserve)}\n"
        return cal