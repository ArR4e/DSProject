import turtle
from random import randint

def hulknurk(külg, pikkus):
    i = 1
    while i <= 30:
        try:
            for x in range(külg):
                turtle.fd(pikkus)
                turtle.rt(360 / külg)
            turtle.pu()
            turtle.lt(randint(1, 360))
            turtle.fd(randint(1, 200))
            turtle.pd()
            külg = randint(3, 15)
            pikkus = randint(10, 200)
            i += 1
        except:
            break

külg = randint(3, 15)
pikkus = randint(10, 200)

turtle.write(hulknurk(külg, pikkus))
turtle.exitonclick()