from turtle import *
from random import randint

#make a rectangle
def rectangle(a, b):
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)

#make 30 random rectangles in random locations
for i in range(30):
    penup()
    goto(randint(0, 100), randint(0, 100))
    pendown()
    a = randint(0, 100)
    b = randint(0, 100)
    rectangle(a, b)

exitonclick()