from turtle import *

def ruut(length, power):
    if power == 0:
        return
    if power == 1:
        forward(length)
        right(90)
        forward(length)
        right(90)
        forward(length)
        right(90)
        forward(length)
    forward(length)
    ruut(length / 2, power - 1)
        
    


ruut(100, 3)

#Got stuck