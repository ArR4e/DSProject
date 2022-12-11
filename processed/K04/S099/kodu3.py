from turtle import *
from random import randint

def hulknurk(kylgede_arv, kylje_pikkus):
    arv = int(kylgede_arv)
    pikkus = float(kylje_pikkus)
    
    nurk = 180 - ((arv - 2) * 180 / arv)
    i = 0
    while i < arv:
        forward(float(kylje_pikkus))
        left(nurk)
        i += 1

e = 0
speed(0)

while e < 30: 
    x = randint(-200, 200)
    y = randint(-200, 200)
    kyljed = randint(3, 10)
    pikkus = randint(20, 100)
    up()
    goto(x, y)
    down()
    hulknurk(kyljed, pikkus)
    e += 1
exitonclick()

    

    