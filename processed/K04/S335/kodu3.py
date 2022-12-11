from turtle import *
from random import randint

def hulknurk(külg, pikkus):
    nurk = 360 / külg
    joonis = 0
    while joonis < külg:
        forward(pikkus)
        left(nurk)
        joonis += 1
        
def liikumine():
    up()
    forward(randint(20, 100))
    left(randint(10, 290))
    down()

hulknurkade_arv = 0
while hulknurkade_arv < 30:
    hulknurk(randint(3, 12), randint(1, 200))
    liikumine()
    hulknurkade_arv += 1

exitonclick()