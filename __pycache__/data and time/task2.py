#2) Date Format (40)
from datetime import datetime

def format_date(a):
    format = '%Y/%m/%d'
    date = datetime.strptime(a,format)
    print(date)



date_string = "2018/08/09"
print(format_date(date_string))



