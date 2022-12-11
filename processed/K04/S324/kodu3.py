#kuidas saaks genereerida suvalised arvud, mis pole ühtestki vahemikust? Random ja randint võtavad arve vahemikust
from turtle import*
speed(10)
from random import randint


def hulknurgad():
    joonistatud_külgi = 1
    külgede_arv = randint(3, 40)
    nurgad = 360/külgede_arv
    külgede_pikkus = randint(1, 200)
    while joonistatud_külgi <= külgede_arv:
        forward(külgede_pikkus)
        left(nurgad)
        joonistatud_külgi += 1
        
kujundite_arv = 1
while kujundite_arv <= 30:
    hulknurgad()
    kujundite_arv += 1
    up()
    right(randint(1,360))
    forward(randint(1,200))
    down()
exitonclick()
    
