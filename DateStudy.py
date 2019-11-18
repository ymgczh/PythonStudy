# 时间学习
import time
import datetime
import calendar
import FunctionStudy

d = FunctionStudy.timeFunction("时间不等人")
print(d)
a = time.time()
print(type(a))
print(a)

b = int(time.time())
print(b)

c = datetime.date
print(type(c))
print(c)

cal = calendar.month(2019, 11)
print(cal)
print(type(cal))
print(id(cal))

