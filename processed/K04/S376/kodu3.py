from turtle import *
from random import *

def f(külgede_arv, küljepikkus):
    algne_külgede_arv = külgede_arv
    while külgede_arv != 0:
        forward(küljepikkus)
        right(360/algne_külgede_arv)
        külgede_arv -= 1

külgede_arv = 0
küljepikkus = 0
hulknurkade_arv = 30

while hulknurkade_arv != 0:
    hulknurkade_arv -= 1
    külgede_arv = randint(3, 15)
    küljepikkus = randint(10, 100)
    up()
    right(randint(0, 360))
    forward(randint(50, 200))
    down()
    f(külgede_arv, küljepikkus)

exitonclick()