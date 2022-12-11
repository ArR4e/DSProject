from turtle import *
from random import randint

def hulknurk(külgede_arv, küljepikkus):
    nurk = 360 / külgede_arv
    i = 0
    while i < külgede_arv:
        forward(küljepikkus)
        right(nurk)
        i += 1

for i in range(30):
    hulknurk((randint(3,12)), (randint(14,60)))
    up()
    goto((randint(-300,300)), (randint(-150,300)))
    down()

exitonclick()