# sarnaste ruutude fraktal
from turtle import*

def fraktal(sygavus, pikkus):
    if sygavus == 0:
        return
    else:
        forward(pikkus)
        left(90)
        fraktal(sygavus - 1, pikkus / 2)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(sygavus - 1, pikkus / 2)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(sygavus - 1, pikkus / 2)
        right(180)
        forward(pikkus)
        right(90)
        
fraktal(4, 100)