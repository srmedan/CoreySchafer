import datetime

#Example for datetime.time.

#t = datetime.time(9, 30, 43, 100000)
#
#print(t.minute)

#Example for datetime.timedelta
#dt =datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)
#
#tdelta = datetime.timedelta(days=7)
#
#print(dt + tdelta)

#Example alternative constructors

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
