import turtle
t=turtle.Pen()
t.showturtle()
t.width(10)
t.color("blue")
#绘制奥运五环
t.circle(50)


t.color("black")
t.penup()
t.goto(120,0)
t.pendown()
t.circle(50)


t.color("red")
t.penup()
t.goto(240,0)
t.pendown()
t.circle(50)

t.color("yellow")
t.penup()
t.goto(60,-50)
t.pendown()
t.circle(50)


t.color("green")
t.penup()
t.goto(180,-50)
t.pendown()
t.circle(50)
'''
t.forward(300)
t.color("red")
t.left(90)
t.forward(300)
t.goto(0,50)
t.goto(0,0)
t.penup()
t.goto(0,300)
t.pendown()
t.penup()
t.goto(50,50)
t.pendown()
t.circle(100)
'''
'''
for x in range(360):
    t.forward(x)
    t.left(59)
'''
'''
t.write("张昊")
'''