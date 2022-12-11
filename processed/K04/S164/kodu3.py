from turtle import *
from random import randint

def hulknurgad(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_külgi += 1
        

hulknurki = 0
while hulknurki < 30:
    hulknurgad(4, 50)
    hulknurki += 1
    up()
    forward(randint(1, 200))
    left(randint(1, 100))
    down()
    