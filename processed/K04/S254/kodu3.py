from turtle import *
from random import randint
speed(60)

def hulknurk(külgi,pikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgi:
        forward(pikkus)
        left(360/külgi)
        joonistatud_külgi += 1


def juhuslik_koht():
    for i in range(30):
        edasi = randint(10,60)
        pööra = randint(0,360)
        külg = randint(3,10)
        pikkus = randint(10,30)
        
        hulknurk(külg,pikkus)
        
        up()
        forward(edasi)
        left(pööra)
        forward(edasi)
        down()

juhuslik_koht()

exitonclick()