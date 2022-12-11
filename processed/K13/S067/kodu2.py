from turtle import *
def ruut(n, pikkus):
    speed(100)
    color('blue')
    if n == 0:
        return
    for i in range(4):
        forward(pikkus)
        left(90)
        if i < 3:
            ruut(n - 1, pikkus / 2)
        left(180)

ruut(5, 200)
exitonclick()