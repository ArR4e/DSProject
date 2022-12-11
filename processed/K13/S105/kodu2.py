from turtle import *
speed(0)

def ruut(a,b):
    for i in range(b):
        if b==0:
            return
        for i in range(4):
            forward(a)
            left(90)
            if i<3:
                ruut(a/2,b-1)
            left(180)