from turtle import *
import random

def hulknurk(nurkade_arv, küljepikkus):
    nurk = (nurkade_arv - 2) * 180 / nurkade_arv
    while nurkade_arv > 0:
        right(180 - nurk)
        forward(küljepikkus)
        nurkade_arv -= 1

kordusi = 30
while kordusi > 0:
    hulknurk(random.randint(3, 10), random.randint(10, 100))
    up()
    right(random.randint(0, 360))
    forward(random.randint(10, 100))
    down()
    kordusi -= 1

exitonclick()