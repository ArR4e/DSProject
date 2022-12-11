from turtle import *

def fun(aste,pikkus):
    global sd
    
    for i in range(3):
        forward(pikkus)
        
        if aste > 1:
            pikkus/=2
            sd = -sd
            fun(aste-1,pikkus)
            sd = -sd
            pikkus*=2
        right(sd)
    forward(pikkus)
    right(sd)
        
sd = 90
turtle = Turtle()
turtle.speed("fastest")  
  
