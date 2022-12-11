from turtle import *

speed(10)
delay(0)

def fraktal(tase, pikkus):
    if tase >= 1:
        for külg in range(4):
            fd(pikkus)
            left(90)
            if külg != 3:
                fraktal(tase-1, pikkus*0.5)
                rt(180)
        rt(180)
        
        
#fraktal(4, 100)