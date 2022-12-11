from turtle import *

speed(-1)

def fraktal(aste):
    liigu = 3 ** aste
    if aste == 1:
        for i in range(4):
            fd(liigu)
            lt(90)
        rt(90)
    else:
        fd(liigu)
        fraktal(aste - 1)
        fd(liigu)
        fraktal(aste - 1)
        fd(liigu)
        fraktal(aste - 1)
        fd(liigu)
