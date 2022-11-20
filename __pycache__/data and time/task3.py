# Write a function that returns the future date in a format (year/month/day) after the entered number of the
# days (40)
from datetime import datetime, timedelta

def format_date(a):
    format = '%Y/%m/%d'
    date = datetime.strptime(a,format)
    date_40 = date + timedelta(days=40)
    print(f"Input date: {date} \nAfter 40 days {date_40}")

date_string = "2018/08/09"
print(format_date(date_string))




