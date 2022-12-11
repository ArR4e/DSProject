from random import randint
from turtle import*
def hulknurk(külgede_arv, küljepikkus):
    x = (180-((külgede_arv - 2)*180/külgede_arv))
    y = 0
    while y <= külgede_arv:
        forward(küljepikkus)
        right(x)
        y += 1
z = 0
while z <= 30:
    külgede_arv = randint(3, 20)
    küljepikkus = randint(5, 100)
    hulknurk(külgede_arv, küljepikkus)
    up()
    right(randint(0,360))
    forward(randint(50,80))
    down()
    z += 1
exitonclick()
