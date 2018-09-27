#Answer to Time Delta

from datetime import datetime
for t_itr in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print(int(abs((t1-t2).total_seconds())))
    
"""
%a - abbreviated weekday name

%A - full weekday name

%b - abbreviated month name

%B - full month name

%c - preferred date and time representation

%C - century number (the year divided by 100, range 00 to 99)

%d - day of the month (01 to 31)

%D - same as %m/%d/%y

%e - day of the month (1 to 31)

%g - like %G, but without the century

%G - 4-digit year corresponding to the ISO week number (see %V).

%h - same as %b

%H - hour, using a 24-hour clock (00 to 23)

%I - hour, using a 12-hour clock (01 to 12)

%j - day of the year (001 to 366)

%m - month (01 to 12)

%M - minute

%n - newline character

%p - either am or pm according to the given time value

%r - time in a.m. and p.m. notation

%R - time in 24 hour notation

%S - second

%t - tab character

%T - current time, equal to %H:%M:%S

%u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1

%U - week number of the current year, starting with the first Sunday as the first day of the first week

%V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week

%W - week number of the current year, starting with the first Monday as the first day of the first week

%w - day of the week as a decimal, Sunday=0

%x - preferred date representation without the time

%X - preferred time representation without the date

%y - year without a century (range 00 to 99)

%Y - year including the century

%Z or %z - time zone or name or abbreviation

%% - a literal % character
"""