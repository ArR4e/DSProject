from turtle import *
from random import randint

def hulknurk(küljed, küljepikkus):
    n = küljed
    while küljed > 0:
        forward(küljepikkus)
        left(360 / n)
        küljed = küljed - 1
        
        
külg = int(input("Sisestage külgede arv: "))
pikkus = int(input("Sisestage külgede pikkus: "))
hulknurk(külg, pikkus)

i = 29
while i > 0:
    up()
    forward(randint(10,150))
    left(randint(10,90))
    forward(randint(10,150))
    down()
    hulknurk(külg, pikkus)
    i = i - 1

exitonclick()