from turtle import *
from random import randint

def shape(a, b):
    sides = a
    while sides > 0:
        forward(b)
        right(360/a)
        sides -= 1

shapes = 30
speed(0)

while shapes > 0:
    up()
    setpos(randint(-400, 300), randint(-200, 400))
    down()
    shape(randint(3, 10), randint(30, 100))
    shapes -= 1

exitonclick()