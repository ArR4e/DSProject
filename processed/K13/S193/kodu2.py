from turtle import *
def fun(sugavus, pikkus):
    if 1<=sugavus:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i<3:
                fun(sugavus-1, pikkus/2)
            left(180)