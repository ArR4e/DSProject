from turtle import *

def ruut(a, b):
    joonis = 0
    while joonis < a:
        forward(b)
        left(180-(((a-2)*180)/a))
        joonis += 1

a=30
b=50
ruut(a, b)
exitonclick()