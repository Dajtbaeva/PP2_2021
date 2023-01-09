from datetime import datetime
def difference(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime(2003, 3, 7, 8, 5, 0)
date2 = datetime.now()
print('Two date difference in seconds', (difference(date2, date1)))
