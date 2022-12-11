from turtle import *
from random import randint

def kujund(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360/külgede_arv)
        joonistatud_külgi +=1
        
i=0
while i<=30:
    i += 1
    kujund(randint(3,10), randint(20,100))
    up()
    goto(randint(-100, 100),randint(-100, 100))
    down()

exitonclick()




