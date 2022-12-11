import turtle
from random import randint
def joonistaja(karv,kpikkus):
    turtle.penup()
    turtle.setpos(randint(0,300),randint(0,300))
    turtle.pendown()
    for x in range(karv):
        turtle.forward(kpikkus)
        turtle.right(360/karv)
for x in range(30):
    a=randint(3,20)
    b=randint(0,30)
    joonistaja(a,b)
turtle.done()