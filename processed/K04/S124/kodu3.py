from turtle import *
from math import *
from random import randint, randrange, choice

n = randint(3, 15)
a = randint(10, 200)
#c = randrange(left, right)
d = randint(1, 359)

def hulknurk(nurgad, pikkus):
    sisenurkade_summa = (nurgad - 2) * 180
    nurk = sisenurkade_summa / nurgad
    joonistatud_külgi = 0
    while joonistatud_külgi < nurgad:
        forward(pikkus)
        left(180 - nurk)
        joonistatud_külgi += 1
        
#hulknurk(6, 80)

kordade_arv = 0
while kordade_arv < 30:
    n = randint(3, 15)
    a = randint(10, 200)
    #d = randint(1, 359)
    #c = choice(["left", "right"])
    #g = randint(100, 500)
    hulknurk(n, a)
    up()
    #left(d)
    setpos(randint(-200, 200), randint(-200, 200))
    #forward(g)
    down()
    kordade_arv += 1
    