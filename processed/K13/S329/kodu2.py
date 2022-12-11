# 2. Sarnaste ruutude fraktal

from turtle import *

def fraktal(n, pikkus):
    if n == 0:
        return
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(n - 1, pikkus / 2)
            left(180)    

speed(10)
#fraktal(5, 200)
