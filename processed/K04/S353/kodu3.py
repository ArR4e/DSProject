from turtle import *
from random import *
up()
speed(10)
screensize(canvwidth=2000, canvheight=2000)
def kujund(x, y):
    left(randint(0, 359))
    forward(randint(0, 500))
    down()
    left(randint(0, 359))
    y1=y
    while y1>0:
        forward(x)
        right(360/y)
        y1-=1
    up()
    home()
i=30
while i>0:
    kujund(randint(7, 100), randint(3, 10))
    i-=1
home()
exitonclick()     
