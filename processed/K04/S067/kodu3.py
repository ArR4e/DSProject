from turtle import *
import random
def joonista(arv, pikkus):
    speed(50)
    y = 360 / arv
    for i in range(arv):
        forward(pikkus)
        right(y)
        i += 1
k = 0    
while k <= 30:
    arv = random.randint(5, 20)
    pikkus = random.randint(50, 100)
    x = random.randint(10, 500)
    y = random.randint(10, 500)
    penup()
    goto(x,y)
    pendown()
    joonista(arv, pikkus)
    k += 1
exitonclick()