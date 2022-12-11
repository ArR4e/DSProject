from turtle import *
from random import *

külgede_arv = randint(3,12)
külje_pikkus = randint(10,100)
kord = 0

while kord < 30:
    def hulknurk(külgede_arv,külje_pikkus):
        n = 0
        while n < külgede_arv:
            forward(külje_pikkus)
            left(360/külgede_arv)
            n += 1
    hulknurk(külgede_arv,külje_pikkus)
    up()
    forward(randint(50,150))
    left(randint(0,360))
    down()
    külgede_arv = randint(3,12)
    külje_pikkus = randint(10,100)
    kord += 1
    
        