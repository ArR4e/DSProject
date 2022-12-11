from turtle import*
import random

def hulknurk(n,l):
    penup()
    x = random.randrange(500)
    y =random.randrange(500)
    goto(x,y)
    pendown()
    for i in range(n):
        forward(l)
        right(360/n)
    
for i in range(30):
    külgede_arv = random.randint(3,10)
    küljepikkus = random.randint(10,100)
    hulknurk(külgede_arv, küljepikkus)
