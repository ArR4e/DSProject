import turtle
import random

def kujund():
    nr1 = random.randint(-500, 500)
    nr2 = random.randint(-200, 200)
    küljed = random.randint(3, 12)
    küljepikkus = random.randint(10, 50)
    iganurk = 360/küljed
    turtle.pu()
    turtle.setpos(nr1, nr2)
    turtle.pendown()
    i = 1
    while i <= küljed:
        try:
            turtle.forward(küljepikkus)
            turtle.left(iganurk)
            i += 1
        except:
            break
i = 1
while i <= 30:
    try:
        kujund()
        i += 1
    except:
        break
turtle.done()