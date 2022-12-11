from turtle import *
def ruut(pikkus, arv):
    forward(pikkus)
    if arv > 1:
        ruut(pikkus/2, arv-1)
        forward(pikkus)
        ruut(pikkus/2, arv-1)
        forward(pikkus)
        ruut(pikkus/2, arv-1)
        forward(pikkus)
    if arv == 1:
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)