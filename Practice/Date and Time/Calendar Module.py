#Answer to Calendar Module

import calendar
a=input().split()
b=calendar.weekday(int(a[2]),int(a[0]),int(a[1]))
c=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(c[b])