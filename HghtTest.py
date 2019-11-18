import turtle
import math

pen = turtle.Pen()
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

pen.penup()
pen.goto(x1, y1)
pen.pendown()
pen.goto(x2, y2)
pen.goto(x3, y3)
pen.goto(x4, y4)

distince = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
print(distince)
