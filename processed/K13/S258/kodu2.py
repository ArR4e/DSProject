from turtle import *

def pretender(n,m=100):
    if n == 1:
        forward(m)
        right(90)
        forward(m)
        right(90)
        forward(m)
        right(90)
        forward(m)
    elif n > 1:
        forward(m)
        left(90)
        pretender(n-1,m/2)
        left(90)
        forward(m)
        left(90)
        pretender(n-1,m/2)
        left(90)
        forward(m)
        left(90)
        pretender(n-1,m/2)
        left(90)
        forward(m)