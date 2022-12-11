from turtle import *
from random import *
speed(10)

def turt():
    penup()
    goto(randint(-100,100), randint(-100,100))
    pendown()
    Juhuslikkülg = randint(3, 20)
    Juhuslikpikkus = randint(0, 100)
    for külg in range(Juhuslikkülg):
        forward(Juhuslikpikkus)
        right(360/Juhuslikkülg)

counter = 0

while counter < 30:
    turt()
    counter += 1
    
    
exitonclick()
    
