from random import *
from turtle import *

def hulknurk(küljed,pikkus):
    for i in range(küljed):
        forward(pikkus)
        right(360/küljed)

for i in range(30):
    penup()
    goto(randrange(200),randrange(200))
    pendown()
    hulknurk(randrange(20),randrange(30))