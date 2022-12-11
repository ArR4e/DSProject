from turtle import *
import random

def joonista(arv, pikkus):
    nurk = ((arv-2) *180)/arv
    while arv>0:
        speed(0)
        forward(pikkus)
        left(180-nurk)
        arv -= 1
    
    return nurk

n = 30

while n>0:
    arv = random.randrange(2,10)
    pikkus = random.randrange(10,50)
    värv = ["pink", "green", "red", "black", "blue", "orange", "purple"]
    värvus1 = random.choice(värv)
    värvus2 = random.choice(värv)
    color(värvus1, värvus2)
    begin_fill()
    joonista(arv, pikkus)
    end_fill()
    penup()
    kohtx = random.randrange(-300,300)
    kohty = random.randrange(-300,300)
    setpos(kohtx,kohty)
    pendown()
    
    n-=1
    
done()
    
    
    
    