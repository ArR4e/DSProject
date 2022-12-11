from turtle import *

def ruutude_fraktal(küljepikkus, samm):
    speed(100)
    if samm == 1:
        for i in range(4):
            forward(küljepikkus)
            left(90)
            left(180)
        
    else:
        for i in range(4):
            forward(küljepikkus)
            left(90)
            if i < 3:
                ruutude_fraktal(küljepikkus * 0.5, samm - 1)
            left(180)

#ruutude_fraktal(100, 4)
exitonclick()