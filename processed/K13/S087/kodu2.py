from turtle import*

def fraktal(sügavus, küljepikkus):
    for i in range(3):
        forward(küljepikkus)
        if sügavus > 1:
            küljepikkus /= 2
            fraktal(sügavus - 1, küljepikkus)
            küljepikkus *= 2
        left(90)
    forward(küljepikkus)
    right(90)

exitonclick()