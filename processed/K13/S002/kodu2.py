from turtle import *

speed(0)
def fra(p, a):
    if a != 0:
        for i in range(3):
            fd(p)
            left(90)
            fra(p/2, a-1)
            right(180)
        fd(p)
        right(90)
        
fra(100,4)