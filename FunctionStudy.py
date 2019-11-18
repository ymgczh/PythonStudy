import time

def timeFunction(timeStr):
    print("时间函数：" + timeStr)
    print(time.time())
    return time.asctime(time.localtime(time.time()))

a = timeFunction("时间不等人");
print(a)

def ChangeInfo(x):
    x = 10
    return x

a = 2
a = ChangeInfo(a)
print(a)


def change_list(param_list):
    param_list.append([1, 2, 3, 4, 5, 6, 7, 8])
    print(param_list)
    return


listInfo = [10, 20, 30, 40]
change_list(listInfo)
print(listInfo)
