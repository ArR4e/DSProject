from turtle import *
from random import randint

def hulknurk(arv, pikkus):
    joonistatud_külgi = 0
    penup()
    goto(randint(-300, 300), randint(-300, 300)) #koordinaadid valitud selliselt, et iga uue hulknuga joonistamine algaks aknavaates
    pendown()
    while joonistatud_külgi < arv:
        forward(pikkus)
        left(360 / arv)
        joonistatud_külgi += 1

hulknurgad = 0
while hulknurgad < 30:
    random_arv = randint(3, 15) #panin maksimaalseks külgete arvuks 15, et hulknurk näeks välja nagu hulknurk, mitte ring
    #hulknurga minimaalne lubatud külgete arv on 3 (?)
    random_pikkus = randint(10, 100) #maksimaalne pikkus 100, et hulknurk mahuks aknavaatesse (enam-vähem) ja minimaalne 10, et ei oleks liiga väike
    hulknurk(random_arv, random_pikkus)
    hulknurgad += 1

exitonclick()