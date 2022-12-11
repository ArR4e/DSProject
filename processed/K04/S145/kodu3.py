import turtle
import math
import random
t = turtle.Turtle()
hulknurgad = 0

def hulknurk(arv, pikkus):
    sisenurk = (arv - 2) * 180 / arv
    for i in range(arv):
        t.forward(pikkus)
        t.right(180 - sisenurk)
        i += 1
        
while hulknurgad <= 30:
    t.up()
    t.setx(random.randint(-200, 200))
    t.sety(random.randint(-200, 200))
    t.down()
    hulknurk(random.randint(3, 20), random.randint(20, 50))
    hulknurgad += 1
         
turtle.exitonclick()
turtle.done()