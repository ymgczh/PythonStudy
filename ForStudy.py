for letter in 'Python':
    print("当前字幕：", letter)

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print("当前水果：", fruit)

for x in range(100):
    print(x)

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

x, y = 0, 1
while y < 19:
    print(y,end=',')
    x, y = y, x + y
