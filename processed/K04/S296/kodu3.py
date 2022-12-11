from random import randint
from turtle import*
küljed = randint(3,20)
pikkus = randint(5,50)
i = 1
def hulknurgad(küljed,pikkus):
    global i
    while i <= küljed:
        forward(pikkus)
        left(180-(180-360/küljed))
        i = i + 1
i = 1
a = 1
while a <= 30:
    küljed = randint(3,20)
    pikkus = randint(5,50)
    penup()
    right(int(randint(1,180)))
    forward(int(randint(20,80)))
    pendown()
    hulknurgad(küljed,pikkus)
    a = a + 1
    i = 1
    
        
    
    

