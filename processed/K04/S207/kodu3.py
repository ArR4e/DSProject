from turtle import *
from random import randint

def hulknurk(arv, pikkus):
    i = 0
    nurk = 360/arv
    while i <= arv:
        forward(pikkus)
        right(nurk)
        i += 1

n = 0
speed(1000)
while n < 30:
    arv = randint(3,16)
    pikkus = randint(10, 50)
    hulknurk(arv, pikkus)
    up()
    setpos(randint(-400,400),randint(-300,300))
    down()
    n += 1
    
exitonclick()