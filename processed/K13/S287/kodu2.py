from turtle import *

def ruudud(arv):
    speed(0)
    if arv == 0:
        right(90)
        return
    else:
        for i in range(4):
            #ruudud(arv - 1)
            forward(round(100 / (2**(i+1)), 0))
            ruudud(arv - 1)
            left(90)
            #ruudud(arv - 1)

ruudud(4)