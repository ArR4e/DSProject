from turtle import *
import random

def hulknurk(külgede_arv, küljepikkus):
    pöörde_kraad = 360 // külgede_arv
    while külgede_arv > 0:
        forward(küljepikkus)
        left(pöörde_kraad)
        külgede_arv -= 1

i = 30
while i > 0:
    i -= 1
    hulknurk(random.randint(3,10), random.randint(20,100))
    a = random.randint(20,100)
    b = random.randint(1,360)
    c = random.randint(20,100)
    up()
    forward(a)
    left(b)
    forward(c)
    down()
    
exitonclick()