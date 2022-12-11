from turtle import *

def f(pikkus, tase):
    speed(1000)
    if tase == 0:
        return None
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:   
                p = pikkus // 2
                t = tase - 1
                f(p, t)
            left(180)