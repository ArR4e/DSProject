from turtle import *
from random import random, randint

def f(külgede_arv, külje_pikkus):
    j = 0
    while j < külgede_arv:
        forward(külje_pikkus)
        left(360 / külgede_arv)
        j += 1

i = 0
while i < 30:
    külgede_arv = randint(1,50)
    külje_pikkus = randint(10,100)
    
    f(külgede_arv, külje_pikkus)
    up()
    goto(randint(-500,500), randint(-500,500))
    down()

    i += 1

exitonclick()