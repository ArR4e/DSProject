#Hulknurgad

from turtle import *
from random import randint

def hulknurk(küljed, pikkus):
    pendown()
    for m in range(küljed):
        forward(pikkus)
        left(360/küljed)
    penup()

for n in range(30):
    hulknurk(randint(3, 20), randint(10, 300))
    goto(randint(-1000, 1000), randint(-1000, 1000))

exitonclick()    