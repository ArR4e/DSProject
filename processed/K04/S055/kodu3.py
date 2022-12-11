from turtle import *
from random import randint

def hulknurk(kyljed, pikkus):
    down()
    nurk = 360 / kyljed
    for i in range(kyljed):
        forward(pikkus)
        left(nurk)
    up()
    
speed(100)
    
for i in range(30):
    hulknurk(randint(3,10),randint(50,200))
    goto(randint(-400,400),randint(-400,400))

exitonclick()
