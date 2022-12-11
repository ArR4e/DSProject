from turtle import *

def joonista(sygavus, suund = 2):
    global pikkus
    if sygavus > 1:
        forward(pikkus)
        pikkus = int(pikkus/2)
        joonista(sygavus-1)
        pikkus = int(pikkus*2)
        if suund == 0:
            forward(pikkus)
            return 0
        joonista(sygavus, suund-1)
    else:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        return 1


pikkus = 200
speed(10)
joonista(4)