from turtle import *
from random import randint

def hulknurk(kylg_arv, kylg_pikkus):  
    for i in range(kylg_arv):
        forward(kylg_pikkus)
        left(360/kylg_arv)

def kohamuutus():
    up()
    left(randint(1, 200))
    forward(randint(1, 200))
    down()
    

for arv in range(30):
    hulknurk(randint(4, 20), randint(1, 100))
    kohamuutus()

exitonclick()