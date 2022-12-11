import turtle as t
from random import randint

t.speed(10)
t.delay(0)
t.pencolor("blue")
t.width(3)


def hulknurk(n, x):
    for i in range(n):
        t.forward(x)
        t.left(360/n)

for i in range(30):
    nurk = randint(3, 8)
    pikkus = randint(20, 100)
    hulknurk(nurk, pikkus)
    
    t.up()
    t.right(randint(0, 360))
    t.forward(randint(10, 150))
    t.down()
    
t.exitonclick()
    

    