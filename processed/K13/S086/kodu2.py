#Kilpkonnaga joonistab ruutudest koosneva fraktali, kolmes nurgas
from turtle import *
speed(0)

def fraktal(sügavus, pikkus):
    left(90)
    for i in range(3):
        forward(pikkus)
        if sügavus != 1:
            fraktal(sügavus-1, pikkus*0.5)
            left(90)
            continue
        else:
            right(90)
            continue
        
    forward(pikkus)
    
fraktal(6, 200)