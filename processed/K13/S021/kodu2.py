from turtle import *
speed(0)

def fraktal(sügavus, küljepikkus):
    if sügavus == 1:
        for i in range(4):
            forward(küljepikkus)
            right(90)
        left(180)
    else:
        forward(küljepikkus)
        left(90)
        fraktal(sügavus-1, küljepikkus/2)
        forward(küljepikkus)
        left(90)
        fraktal(sügavus-1, küljepikkus/2)
        forward(küljepikkus)
        left(90)
        fraktal(sügavus-1, küljepikkus/2)
        forward(küljepikkus)
        left(90)
      
fraktal(4, 100)

exitonclick()
        