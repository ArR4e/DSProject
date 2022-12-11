from turtle import *
from random import randint

def kujund(x, y):
    nurk = round(((x-2) * 180) /x)
    while x > 0:
        forward(y)
        left(180 - nurk)
        x -= 1
 
z = 30
while z > 0:
    up()
    forward(randint(10, 20))
    right(randint(5,30))
    forward(randint(10, 20))
    down()
    kujund(randint(3,12), randint(20, 100))
    z -= 1