from turtle import *

def fraktal(tase, pikkus):
    if tase>=1:
        fraktal(tase-1, 0.7*pikkus)
        for i in range(2):
            lt(120)
            fd(pikkus)
        lt(120)
        fd(pikkus)
        backward(pikkus)