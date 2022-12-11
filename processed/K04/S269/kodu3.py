import turtle
import random


def hulknurk(n,l):
    a = n
    while a > 0:
        turtle.forward(l)
        turtle.left(360/n)
        a-=1
        



for i in range(30):
    turtle.pu()
    x = random.uniform(-turtle.window_width()/2,turtle.window_width()/2)
    y = random.uniform(-turtle.window_height()/2,turtle.window_height()/2)
    turtle.setposition(x, y)
    turtle.pd()
    hulknurk(random.randint(3, 12), random.uniform(1, turtle.window_height()/7))
    
exitonclick()