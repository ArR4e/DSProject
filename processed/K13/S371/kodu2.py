from turtle import *

def ruut(tase, pikkus):
    for i in range(3):
        forward(pikkus)
        if tase > 1:
            left(90)
            ruut(tase - 1, pikkus * 0.5)
            right(90)
        right(90)
    forward(pikkus)
    right(90)
    
            

delay(0)
ruut(4, 100)
exitonclick()