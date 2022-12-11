from turtle import *
speed(-1)

def fraktal(tase, pikkus):
    if tase == 1:
        for x in range(4):
            fd(pikkus)
            lt(90)
    else:
        for x in range(3):
            fd(pikkus)
            fraktal(tase-1,pikkus/2)
            rt(90)
        fd(pikkus)
        lt(90)
       
fraktal(7, 100)