import turtle
import random
def hulknurk(n, l):
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360/n)
for i in range(30):
    l=random.randint(50,300)
    n=random.randint(3,10)
    hulknurk(n, l)
    turtle.penup()
    turtle.goto(random.randint(-400,400), random.randint(-400,400))
    turtle.pendown()


    