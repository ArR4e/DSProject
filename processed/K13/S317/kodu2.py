from turtle import *
def ruut(sügavus,pikkus):
    for i in range(4):
        turtle.speed(0)
        turtle.forward(120)
        turtle.left(90)
        if i < 3:
            for i in range(4):
                turtle.forward(80)
                turtle.left(90)
                if i < 3:
                    for i in range(4):
                        turtle.forward(40)
                        turtle.left(90)
                        if i < 3:
                            for i in range(4):
                                turtle.forward(15)
                                turtle.left(90)
                                turtle.left(180)
                        turtle.left(180)
                turtle.left(180)
        turtle.left(180)
def ruutõige(sügavus):
    if sügavus == 0:
        return 0
    for i in range(4):
        turtle.forward(120)
        turtle.left(90)
        for i in range(4):
            turtle.forward(120)
            turtle.left(90)
        turtle.left(90)
        return ruutõige(sügavus-1)

def fraktal(sügavus, pikkus):
    if sügavus > 0:
        for i in range(3):
            forward(pikkus)
            left(90)
            fraktal(sügavus-1,pikkus*0.4)
            left(180)
        forward(pikkus)
        right(90)
speed(0)
delay(0)
fraktal(5,100)
exitonclick()
        