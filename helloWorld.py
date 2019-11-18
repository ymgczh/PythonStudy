# 一切皆对象
a = 3
print(a)
print(id(a))
print(type(a))

MAP_SPEED = 120
print(MAP_SPEED)

print(id(MAP_SPEED))
print(type(MAP_SPEED))

b = MAP_SPEED // a
print(b)
print(type(b))

c = MAP_SPEED % a
print(c)
