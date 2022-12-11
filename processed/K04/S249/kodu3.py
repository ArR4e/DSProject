from turtle import *
from random import randint

def külg(arv, pikkus):
    i = arv
    while arv > 0:
        forward(pikkus)
        right(360 / (i) )
        arv -= 1
        
i = 0
while i < 30:
    külg(randint(3,8), randint(10, 50))
    i += 1
    penup()
    goto(randint(-220, 0), randint(0, 220))
    pendown()
exitonclick()
    
    