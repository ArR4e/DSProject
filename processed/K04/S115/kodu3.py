from turtle import*
from random import randint

def hulknurk(külgede_arv, küljepikkus):
    joonistatud = 0
    while joonistatud < külgede_arv:
        forward(küljepikkus)
        left(75)
        forward(küljepikkus)
        left(60)
        joonistatud += 1

i = 0
while i < 30:
    külgede_arv = randint(3, 13)
    küljepikkus = randint(1,50)
    hulknurk(külgede_arv, küljepikkus)
    up()
    forward(100)
    left(90)
    forward(100)
    down()
    i += 1
        
exitonclick()