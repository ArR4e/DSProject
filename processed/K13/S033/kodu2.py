from turtle import *

speed(100)

def ruut_fraktal(tase, pikkus):
    if tase > 1:
        forward(pikkus)
        left(90)
        ruut_fraktal(tase-1, 0.4*pikkus)
        left(90)
        forward(pikkus)
        left(90)
        ruut_fraktal(tase-1, 0.4*pikkus)
        left(90)
        forward(pikkus)
        left(90)
        ruut_fraktal(tase-1, 0.4*pikkus)
        left(90)
        forward(pikkus)
    elif tase == 1:
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)

print(ruut_fraktal(5, 100))
    