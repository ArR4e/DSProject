from turtle import *

def fraktal(n, kulg):
    if n == 0:
        print()
    else:
        fd(kulg)
        lt(90)
        fraktal(n-1, kulg/2)
        rt(180)
        fd(kulg)
        rt(90)
        fd(kulg)
        rt(90)
        fd(kulg)
        rt(90)