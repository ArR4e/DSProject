from turtle import *
from random import randint
i = 0

def hulknurk():
    pikkus = float(input('Pikkus on: '))
    kylg = float(input('Kylgi on: '))
    joonistatud = 0
    while joonistatud < kylg:
        forward(pikkus)
        left(360/kylg)
        joonistatud += 1

def muutus():
    up()
    forward(randint(0, 100))
    left(randint(0, 360))
    forward(randint(0, 100))
    down()

while i < 30:
    hulknurk()
    muutus()
    i += 1

exitonclick()