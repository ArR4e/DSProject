from turtle import *

def ruudud(sygavus,n):
    for i in range(3):
        forward(n)
        if sygavus > 1:
            ruudud(sygavus -1,n/2)
        
        left(90)
    
    forward(n)
    right(90)

exitonclick()