from turtle import *

def ruut(k,p):
    if k == 0:
        return
    else:
        for i in range(4):
            forward(p)
            left(90)
            if i < 3:
                ruut(k-1,p/2)
            left(180)