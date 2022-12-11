from turtle import *
from random import randint

def hulknurk(kuljed, pikkus):
    joonistatud_kulgi = 0
    nurkadesumma = (kuljed - 2) * 180
    alfa = nurkadesumma/kuljed
    while joonistatud_kulgi < kuljed:
        forward(pikkus)
        right(alfa - 180)
        joonistatud_kulgi += 1

korrad = 0

while korrad <= 30:
    penup()
    goto(randint(-500, 500), randint(-500, 500))
    pendown()
    hulknurk(randint(3, 16), randint(1, 300))
    korrad += 1
    penup()
    goto(0, 0)