#ex1
import datetime

x=datetime.datetime.now()
y=x-datetime.timedelta(days=5)

y_date = y.date()
print(y_date)
#ex2
import datetime

x=datetime.datetime.now()
y=x-datetime.timedelta(days=1) 
z = x+datetime.timedelta(days=1)

y_date = y.date()
x_date = x.date()
z_date = z.date()
print(y_date , x_date , z_date )

#ex3
import datetime

x=datetime.datetime.now()
y = x.replace(microsecond=0)
print(y)
#ex4
import datetime

def d(date1, date2):
    timedelta = date2 - date1
    return timedelta.total_seconds()

date_format = "%y-%m-%d %H:%M:%S"


x = input("Input1: ")
y = input("Input2: ")

date1 = datetime.datetime.strptime(x, date_format)
date2 = datetime.datetime.strptime(y, date_format)

dif =int(d(date1, date2)) 
if dif<0:
    dif=-dif
print("Difference in seconds:", dif)