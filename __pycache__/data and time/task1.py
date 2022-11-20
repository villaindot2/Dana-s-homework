#1) Write function that returns today's date in a format (day.month.year) (30)

import datetime

def currentdate(string):
    now = datetime.datetime.now()  
    return print (now.strftime(string)) 
a = 'Current date: %d.%m.%Y'
print(currentdate(a))

