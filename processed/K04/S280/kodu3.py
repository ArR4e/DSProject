# 3. Hulknurgad / RP
from math import *
from random import *
from turtle import *

def hulknurk(külgede_arv, küljepikkus):
    kraad = 180 - ((külgede_arv - 2) * 180) / külgede_arv
    for x in range(külgede_arv):
        fd(küljepikkus)
        lt(kraad)

for x in range(30):
    küljed = randint(3, 40)
    pikkus = randint(10, 50)
    up()
    goto(randint(-350, 100), randint(-350, 100))
    down()
    hulknurk(küljed, pikkus)

exitonclick()