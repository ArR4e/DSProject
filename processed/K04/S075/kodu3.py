from turtle import *
from random import randint

def hulknurk(arv,pikkus):
    n=0
    nurk=360/arv
    while n<arv: 
        forward(pikkus)
        left(nurk)
        n +=1

#arv=int(input("Mitu külge? "))
#pikkus=int(input("Kui pikkad küljed? "))
s=0


while s<30:
    arv=randint(3,20)
    pikkus=randint(1,90)
    hulknurk(arv,pikkus)
    up()
    goto(randint(-300,300),randint(-300,300))
    down()
    s +=1

exitonclick( )