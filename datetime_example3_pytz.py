import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)

print(dt_now)

#alternative
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)