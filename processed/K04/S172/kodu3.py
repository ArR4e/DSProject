from turtle import *
from random import randint

def hulknurk(n, side):
    n = float(n)
    side = float(side)
    nurk = 360/n
    i = 0
    while i < n:
        forward(side)
        left(nurk)
        i+=1
        
a = 0
while a < 30:
    n = randint(3, 10)
    pikkus = randint(10, 30)
    x = randint(-200, 200)
    y = randint(-200, 200)
    up()
    goto(x,y)
    down()
    hulknurk(n, pikkus)
    a +=1