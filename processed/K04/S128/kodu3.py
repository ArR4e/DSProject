#Hulknurgad
from turtle import *
from random import randint

def hulknurk(arv, pikkus):
    nurkade_summa = (arv-2)*180
    nurk = nurkade_summa/arv
    up()
    goto(randint(-200,200), randint(-200,200))
    down()
    for i in range(arv):
        forward(pikkus)
        right(180-nurk)
n=0
while n<30:
    külgede_arv = randint(3,30)
    külgede_pikkus = randint(3,30)
    hulknurk(külgede_arv, külgede_pikkus)
    n += 1
exitonclick()