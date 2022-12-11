from turtle import *
from random import randint
speed(1000)

def kujund():
    joonistatud_külgi = 0
    külgede_arv = randint(3, 40)
    küljepikkus = randint(1,50)
    while joonistatud_külgi < (külgede_arv):
        forward(küljepikkus)
        right(360/külgede_arv)
        joonistatud_külgi += 1
        


#tekib kujund
kujundite_arv = 0
while kujundite_arv < 30:
    down()
    kujund()
    up()
    edasiminek = randint(1,50)
    forward(edasiminek)
    keere = randint(1, 360)
    right(keere)
    forward(edasiminek)
    
    forward(edasiminek)
    kujundite_arv += 1
    

exitonclick()