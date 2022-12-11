from turtle import *
from random import randint

külgedearv = randint(4,9)
küljepikkus = randint(1,100)

def hulknurgad(külgedearv,küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgedearv:
        forward(küljepikkus)
        left(360/külgedearv)
        joonistatud_külgi += 1
    area = Screen()
    


kujundeid=0
while kujundeid <30:
    külgedearv = randint(4,9)
    küljepikkus = randint(1,100)
    edasi=randint(1,200)
    vasakule=randint(0,180)
    up()
    forward(edasi)
    left(vasakule)
    down()
    hulknurgad(külgedearv,küljepikkus)
    kujundeid= kujundeid+1