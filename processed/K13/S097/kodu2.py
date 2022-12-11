from turtle import*

def fraktal(sügavus, pikkus):
    forward(pikkus)
    for i in range(3):
        if sügavus > 1:
            fraktal(sügavus-1, 0.5*pikkus)
            right(90)
            forward(pikkus)
        else:
            right(90)
            forward(pikkus)
    left(90)

exitonclick()