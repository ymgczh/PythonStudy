import time
time1 = time.time()
# 字符 , 不可变
print(ord("张"))
print(ord("昊"))
a = 'xst'
# my_name = input("请输入名字")

b = ""
for i in range(100):
    a += "sxt"

time2 = time.time()
print(a)
print("time:" + str(time2 - time1))

li = []
for i in range(1000):
    li.append("atb")

a = "".join(li)
print(a)