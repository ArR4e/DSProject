from turtle import *

def fraktal(tase,pikkus):
    for i in range(4):
            forward(pikkus)
            if tase == 1:
                left(90)
                left(180)
            elif i<3:
                left(90)
                fraktal(tase-1, pikkus*0.5)
                left(180)
            else:
                left(90)
                left(180)
                
        