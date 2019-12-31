
import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

print(tday - tdelta)

bday = datetime.date(2020, 9, 24)

till_bday = bday - tday

print(till_bday.total_seconds())