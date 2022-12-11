from turtle import *
from random import randint
import random

kogus = 0
küljed = randint(3,9)
pikkus = randint(5,30)

def hulknurk(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_külgi += 1
        if joonistatud_külgi == külgede_arv:
            up()
            setx(randint(-300,300))
            sety(randint(-300,300))
            down()
            
while kogus < 30:
    hulknurk(küljed,pikkus)
    kogus += 1
    küljed = randint(3,9)
    pikkus = randint(5,30)
    
exitonclick()