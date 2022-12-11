from turtle import *
from random import *

def hulknurk(küljed,pikkus):
    s = (küljed - 2) * 180 #sisenurkade summa
    pööre = s / küljed #iga nurk 
    n = küljed
    
    while n > 0:
        forward(pikkus)
        left(180-pööre)
        n -= 1
        
i = 30    
while i > 0:

    Külg = randint(3,10)
    Pikkus = randint(5,60)
    hulknurk(Külg,Pikkus)

    penup()
    
    goto(randint(-500,500),randint(-500,500))
    
    pendown()
    i -= 1

   
    

