from turtle import *
import random


def hulknurk(arv, pikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < arv:
        forward(pikkus)
        left(((arv-2)*180) / arv)
        forward(pikkus)
        left(180 - (((arv-2)*180) / arv))
        joonistatud_külgi += 2
    
    # liigume järgmisesse kohta
    up()
    forward(10*(random.randint(3, 10)))
    left(90-pikkus)
    forward(10*(random.randint(1, 5)))
    down()
    


count = 0
while count < 30:
    arv = random.randint(3, 10)
    pikkus = random.randint(100, 200)
    hulknurk(arv, pikkus)
        
    count = count + 1
    

exitonclick()

    
    
    
    
    