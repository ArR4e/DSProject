from turtle import *

def fraktal(külg, sügavus):
    if sügavus == 0:
        return done()
    else:
        for i in range(4):
            if i < 3:
                for el in range(3):
                    forward(külg/2)
                    right(90)
            return fraktal(külg/2, sügavus-1)
            
fraktal(300, 4)
