from turtle import *
from random import randrange
def hulknurk(nurkade_arv, küljepikkus):
    x = nurkade_arv
    while x > 0:
        forward(küljepikkus)
        left(180 - (nurkade_arv - 2) * 180 / nurkade_arv)
        x -= 1
    return
    
def kohavahetus(küljepikkus):
    up()
    z = randrange(0, 360)
    left(z)
    y = randrange(küljepikkus, 200)
    forward(y)
    down()
    return

    
a = randrange(3, 10)
b = randrange(10, 40)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)

hulknurk(a, b)

kohavahetus(b)


exitonclick()