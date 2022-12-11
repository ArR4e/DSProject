from turtle import *

def kujund(n, pikkus):
    for _ in range(4):
        fraktal(n, pikkus)
        left(90)

def fraktal(n, pikkus):
    if n == 1:
        forward(pikkus)
        left(90)
    else:
        fraktal(n - 1, pikkus * 2)
        forward(pikkus)
        left(90)

kujund(3, 25)
exitonclick()