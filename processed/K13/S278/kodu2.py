from turtle import *
def funktsioon(dep, pikkus):
    if 1 <= dep:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                funktsioon(dep-1, pikkus/2)
            left(180)
speed(0)
funktsioon(4, 100)