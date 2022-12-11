from turtle import *
from random import *

def hulknurk():
    küljed = randint(3, 15)
    pikkus = randint(1, 50)
    for külg in range(küljed):
        forward(pikkus)
        left(360/küljed)


hulknurk()

exitonclick()