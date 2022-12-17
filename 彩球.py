import turtle as t
t.speed(0)
#随机数
import random


t.colormode(255)


#整体缩进:全选按tab键
for i in range(30):
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)

    x=random.randint(-450,450)
    y=random.randint(-100,250)


    t.penup()
    t.goto(x,y)
    t.pendown()

    t.color(red,green,blue)
        
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.right(90)
    t.forward(50)
    t.left(90)

#RGB red green blue（三原色）
