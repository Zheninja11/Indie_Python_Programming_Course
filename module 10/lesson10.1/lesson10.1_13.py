import datetime
import types

start_date = datetime.date(2022, 1, 1)

def generate_days():
   for i in range(1, 78):
       yield (i, (start_date + datetime.timedelta(days=i-1)).strftime('%A'))

days = generate_days()

for day in days:
   print(day)
   if day[0] == 77:
       break

assert isinstance(days, types.GeneratorType), 'Вы не создали генератор в переменной days'
