from turtle import*
from random import*
def hulknurk(n, a):
    nurk = 180 - ((180 * (n - 2) / n))
    while n > 0:
        forward(a)
        left(nurk)
        n-=1
n = randint(3,30)
a = randint(20,150)
x = randint(3,30)

while x < 30:
        hulknurk(n, a)
        penup()
        left(90)
        forward(randint(50,500))
        pendown()
        x+=1
exitonclick()

    