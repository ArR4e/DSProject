from turtle import *
from random import randint

k = 1

while k < 31:
    k += 1
    külgede_arv = randint(3, 20)
    küljepikkus = randint(15, 50)
    
    def hulknurk(külgede_arv, küljepikkus):
        i = 0
        nurk = 360 / külgede_arv
        while (i < külgede_arv):
            forward(küljepikkus)
            left(nurk)
            i = i + 1
            
    hulknurk(külgede_arv, küljepikkus)
    
    up()
    left(randint(0, 360))
    forward(randint(0, 150))
    down()
    
exitonclick()
