import datetime
import importlib

bday_message = importlib.import_module('41_1_bday_message')

today = datetime.date.today()
next_birthday = datetime.date(today.year, 2, 26)
days_away = (next_birthday - today).days

if today == next_birthday:
  print(bday_message.random_message)
else:
  print(f"My next birthday is {days_away} days away!")