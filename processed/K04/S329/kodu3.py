import turtle
import random

def hulknurk(n, pikkus):
    t = random.randint(50,200)
    summa=(n-2)*180
    if summa%n==0:
        angle=summa//n
        for i in range(n):
            turtle.forward(t)
            turtle.left(180-angle)
turtle.speed(5)
a = 0
while a < 30:
    a = a + 1
    print(a)
    hulknurk(random.randint(3, 8), random.randint(3, 8))
    turtle.up()
    turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
    turtle.down()
        