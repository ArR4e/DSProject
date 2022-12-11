import turtle
import random

k = 0

turtle.penup()
turtle.speed(2000)

def hulknurk(arv, pikkus):
    
    i = 0
    nurk = 360 / arv
    
    while i <= arv:
        
        turtle.forward(pikkus)
        turtle.left(nurk)
        
        i += 1

while k < 30:
    
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    turtle.goto(x, y)
    
    turtle.pendown()
    
    arv = random.randint(3,10)
    pikkus = random.randint(3,100)
    hulknurk(arv, pikkus)
    
    turtle.penup()
    
    k += 1
    
turtle.exitonclick()