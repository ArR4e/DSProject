# Hulknurgad

from turtle import *
from random import random, randint




def hulknurgad(n, l):
    sisenurk = 180 - ((n-2)*180)/n
    while n > 0:
        forward(l)
        right(sisenurk)
        n -= 1

x = 30

speed(0)
delay(5)

while x >= 0:
    pensize(randint(1, 10))
    pencolor(random(),random(),random())
    penup()
    goto(randint(-700, 700), randint(-200, 500))
    pendown()
    hulknurgad(randint(3, 10), randint(10, 100))
    x -= 1

exitonclick()