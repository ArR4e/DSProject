from turtle import *
from random import *

def hulknurk(küljed, pikkus):
    nurk = 180 - ((180*(küljed-2))/küljed)

    while küljed > 0:
        speed(100)
        forward(pikkus)
        left(nurk)
        küljed = küljed - 1
        

x=0    
küljed = randint(3, 30)
pikkus = randint(10,100)

while x < 30:
    hulknurk(küljed, pikkus)
    x += 1
    up()
    left(randint(0,360))
    forward(randint(0,200))
    down()
    
