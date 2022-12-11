from turtle import *
from random import randint

i=1
delay(0)

def hulknurk(n,a):
    joonistatud_kylgi = 0
    while joonistatud_kylgi <= n:
        forward(a)
        left(360/n)
        joonistatud_kylgi+=1


while i <= 30:
    kyljed = randint(3, 8)
    pikkus = randint(10,50)
    hulknurk(kyljed,pikkus)
    r = randint(100,200)
    up()
    forward(r)
    left(kyljed)
    down()
    i+=1



exitonclick()