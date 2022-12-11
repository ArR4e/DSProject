from turtle import *
from random import randint
def küljed(arv, pikkus):
    a = 180-(180*(arv -2))/arv
    for i in range(arv):
        forward(pikkus)
        right(a)

for i in range(30):
    arv = randint(3,12)
    pikkus = randint(50,100)
    küljed(arv, pikkus)
    up()
    x= randint(-200,200)
    y= randint(-200,200)
    goto(x,y)
    down()