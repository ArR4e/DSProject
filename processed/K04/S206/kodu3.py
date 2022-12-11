from turtle import *
from random import *

def hulknurk(kylg, pikkus):
    nurk = 360/kylg
    while kylg > 0:
        forward(pikkus)
        right(nurk)
        kylg -= 1

i = 1

while i <= 30:
    penup()
    goto(randint(-250, 250), randint(-250, 250))
    pendown()
    hulknurk(randint(3,16), randint(10,100))
    i += 1
exitonclick()