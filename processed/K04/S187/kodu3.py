from turtle import *
from random import randint

def kujund(n, s):
    nurk = 180 - ((n - 2) * 180)/n
    Turtle
    down()
    for i in range(0, n):
        forward(s)
        right(nurk)

for i in range(0, 30):
    kujund(randint(3, 10), randint(20, 100))
    up()
    right(randint(0, 360))
    forward(randint(50, 100))

# Kutsuge mind nüüd Picassoks ja tehke mulle minu oma muuseum