""" You are given the following information,
    but you may prefer to do some research for yourself.

        * 1 Jan 1900 was a Monday.
        *   Thirty days has September,
            April, June and November.
            All the rest have thirty-one,
            Saving February alone,
            Which has twenty-eight, rain or shine.
            And on leap years, twenty-nine.
        * A leap year occurs on any year evenly divisible by 4,
          but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during
    the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def leap_year(year):
    return (year%400 == 0) or (year%4 == 0 and year%100 != 0)

def day_in_week(day, mounth, year):
    # Zeller's algorithm
    d = day
    m = (mounth - 3) % 12 + 3   # mounths go from 3 to 14 (march to february)
    if m > 12:
        year -= 1   # january and february belong to the previous year
    
    y = year % 100  # last 2 digits of year
    c = year // 100 # first 2 digits of year
    w = (d + (13*(m+1))//5 + y + y//4 + c//4 - 2*c) % 7
    return w        # 1=sunday, 0=saturday


days_in_mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day, mounth, year = 1, 1, 1901  
count_sundays = 0
while year < 2001:
    if day == 1 and day_in_week(day, mounth, year) == 1:
        count_sundays += 1
    day += 1
    if day > days_in_mounth[mounth-1]:
        day = 1
        mounth += 1
    if mounth > 12:
        mounth = 1
        year += 1
        days_in_mounth[1] = 29 if leap_year(year) else 28

print(count_sundays)
