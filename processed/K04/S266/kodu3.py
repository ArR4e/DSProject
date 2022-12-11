from turtle import*
from random import*

def hulknurk(külgede_arv, külje_pikkus):
    nurk = 360 / külgede_arv
    x = 0
    while x < külgede_arv:
        forward(külje_pikkus)
        right(nurk)
        x += 1
    
arv = randint(4, 20)
pikkus = randint(50, 200)
i = 0 
while i < 30:
    hulknurk(arv, pikkus)
    up()
    left(randint(0,360))
    forward(randint(0, 500))
    down()
    i += 1
    
    