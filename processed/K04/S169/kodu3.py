import turtle as t
from random import *

t.speed(0)

def hulknurk(külgedearv, küljepikkus):
    nurk = ((külgedearv-2)*180)/külgedearv
    for a in range(külgedearv):
        t.fd(küljepikkus)
        t.right(180-nurk)
        
for a in range(30):
    t.penup()
    t.goto(randint(-300,300),randint(-200,400))
    t.pendown()
    hulknurk(randint(3,20),randint(1,100))

t.exitonclick()