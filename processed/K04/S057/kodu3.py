from turtle import *
from random import *

külgede_arv = randint(3,10)
küljepikkus = randint(50,100)
def kilpkonn(külgede_arv, küljepikkus):
    külgede_arv = randint(3,10)
    küljepikkus = randint(10,75)
    kaugus = randint(75,300)
    juhuslik_nurk = randint(1,360)
    nurk = 360 / külgede_arv
    u = 0
    
    up()
    forward(kaugus)
    right(juhuslik_nurk)
    down()
    while u < külgede_arv:
        forward(küljepikkus)
        right(nurk)
        u += 1
    
i = 0
while i < 30:
    kilpkonn(külgede_arv, küljepikkus)
    i += 1

exitonclick()