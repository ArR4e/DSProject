import turtle
from random import randint
def kujund(a, b):
    turtle.Turtle()
    for _ in range(a):
        turtle.forward(b)
        turtle.right(360 / a)
        
turtle.speed(8)
i = 0
while i<30:
    n = randint(3, 15)
    l = randint(0, 100)
    o = randint(-400, 0)
    p = randint(0, 400)
    turtle.pendown()
    kujund(n, l)
    turtle.penup()
    turtle.goto(o, p)
    i = i+1
turtle.exitonclick()