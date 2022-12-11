from turtle import *
from random import randint
def hulknurk(küljed, pikkus):
    sisenurk = 180-180*(küljed-2)/küljed
    print(sisenurk)
    for i in range(küljed):
        forward(pikkus)
        left(sisenurk)
hulknurk(9, 20)
for i in range(30):
    x = randint(-300, 300)
    y = randint(-300, 300)
    up()
    goto(x, y)
    down()
    külgedeArv = randint(3, 12)
    küljePikkus = randint(10, 60)
    hulknurk(külgedeArv, küljePikkus)
    