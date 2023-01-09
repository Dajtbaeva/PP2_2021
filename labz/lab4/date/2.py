import datetime
print('Yesterday :', datetime.date.today() - datetime.timedelta(days = 1))
print('Today :', datetime.date.today())
print('Tomorrow :', datetime.date.today() + datetime.timedelta(days = 1))