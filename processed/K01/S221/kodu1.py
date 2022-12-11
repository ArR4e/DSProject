from turtle import *
import turtle
t = turtle
speed(0)
up()
goto(-500, -150)


down()
forward(1000)
up()
goto(0, -150)
down()

t.fillcolor("red")
t.begin_fill()
forward(200)
left(55)
forward(60)
left(125)
forward(400)
left(125)
forward(60)
turtle.end_fill()




up()
left(55)
forward(60)
left(90)
forward(50)
down()
forward(50)
right(90)
forward(250)
right(90)
forward(52)
right(180)
forward(52)
left(90)
forward(34)
t.fillcolor("red")
t.begin_fill()
right(90)
forward(60)
left(90)
forward(15)
left(90)
forward(60)
turtle.end_fill()
t.fillcolor("red")
t.begin_fill()
right(90)
forward(90)
right(90)
forward(45)
left(90)
forward(12)
left(90)
forward(45)
turtle.end_fill()

t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.forward(50)
    t.right(144)
turtle.end_fill()

#Poola laev
exitonclick()