from turtle import *



def hulknurk(küljed, pikkus):
    i = 0
    while i < küljed:
        forward(int(pikkus))
        left(360/küljed)
        i += 1

from random import randint

i = 0
while i <= 30:
    küljed = randint(3,100)
    pikkus = randint(1,100)
    hulknurk(küljed, pikkus)
    penup()
    goto((randint(-100,0)),(randint(-100,0)))
    pendown()
    i += 1
        
    
        
    