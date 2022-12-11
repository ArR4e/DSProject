#2. sarnaste ruutude fraktal

from turtle import *

def fraktal(sügavus, külg):
#     if sügavus==0:
#         return left(90)
    if sügavus==1:
        for n in range(4):
            forward(külg)
            right(90)
        return 0
    else:
        for n in range(4):
            forward(külg)
            left(90)
            if n<3:
                fraktal(sügavus-1, külg*0.5)
                left(180)
        return left(180)
    exitonclick()

#fraktal(7, 90)

