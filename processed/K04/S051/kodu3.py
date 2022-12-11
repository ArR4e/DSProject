from turtle import *
from random import randint

def hulknurk(külgede_arv, külje_pikkus):
    nurga_suurus = (külgede_arv - 2) * 180 / külgede_arv
    i = 0
    while i < külgede_arv:
        forward(külje_pikkus)
        left(180-nurga_suurus)
        i += 1
    left(180-nurga_suurus)
    return

j = 0
while j < 30:
    up()
    forward(randint(10, 200))
    left(randint(0, 360))
    down()
    
    # Selleks, et kujundid liiga suured ekraani jaoks poleks, peavad mingid piirangud olema.
    arv = randint(3, 30)
    pikkus = randint(5, 100)
    
    hulknurk(arv, pikkus)
    j += 1

exitonclick()