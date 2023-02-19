
from datetine import datetime

def string_to_date(date):
  return datetime.strptime(date, '%d-%m-%Y  %H:%M:%S')
 
