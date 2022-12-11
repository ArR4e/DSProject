from random import randint
from turtle import *

def korrapärane_hulknurk(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_külgi += 1

hulknurkade_arv = 0

while hulknurkade_arv < 30:
    külgede_arv = randint(3, 15)
    küljepikkus = randint(50, 100)
    korrapärane_hulknurk(külgede_arv, küljepikkus)
    up()
    forward(150)
    left(90)
    forward(200)
    down()
    hulknurkade_arv += 1

exitonclick()
        