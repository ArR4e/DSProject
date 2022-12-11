from turtle import *

def funktsioon(pikkus, aste):
    if aste >= 1:
        for i in range(4):
            fd(pikkus)
            if i < 3:
                funktsioon(pikkus*0.5, aste-1)
            left(nurk)
        left(180)