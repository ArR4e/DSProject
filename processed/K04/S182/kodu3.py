from turtle import *
from random import randint
def küljed (küljearv, küljepikkus):
    joontearv=0
    while joontearv < küljearv:
        forward(küljepikkus)
        left(360/küljearv)
        joontearv +=1

kujundid=0
while kujundid < 30:
    küljearv=randint(3,20)
    küljepikkus=randint(50,100)
    küljed (küljearv, küljepikkus)
    up()
    goto(randint(0,100),randint(0,100))
    down()
    kujundid +=1
exitonclick()

