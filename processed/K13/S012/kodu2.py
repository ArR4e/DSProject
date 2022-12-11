#nädal 13 - kodutöö 2
from turtle import *

def fraktal(n, külg):
    if n == 1:
        for i in range(4):
            forward(külg)
            left(90)
            left(180)
    else:
        for i in range(4):
            forward(külg)
            left(90)
            if i < 3:
                fraktal(n-1, külg/2)
            left(180)
           



    