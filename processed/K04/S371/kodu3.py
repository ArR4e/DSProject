from turtle import *
from random import *

def kolmnurk(külgede_arv, küljepikkus):

    for i in range(30):
        penup()
        goto(randint(-300, 300), randint(-300, 300))
        pendown()
        
        for i in range(külgede_arv):
            nurk = 360 / külgede_arv
            forward(küljepikkus)
            left(nurk)

kolmnurk(randint(3, 10), randint(10, 50))

exitonclick()