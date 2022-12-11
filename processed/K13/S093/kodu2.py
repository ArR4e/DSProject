from turtle import *

def fraktaal(n):
    lenght = 10 ** (n/2)
    if n == 0:
        return
    
    forward(lenght)
    for i in range(3):
        fraktaal(n-1)
        if n == 1:
            right(90)
        forward(lenght)
        
speed(4)
fraktaal(4)
