from datetime import datetime
import calendar
dt = datetime.now()
y, m, d = dt.year, dt.month, dt.day
while m != 13:
    c = 0
    for wek in calendar.monthcalendar(y, m):
        if wek[3] != 0 and wek[3] >= d :
            c += 1
        if c == 3:
            print(datetime.strftime(datetime(y, m, wek[3]), '%d.%m.%Y'))
    m += 1
    d = 1