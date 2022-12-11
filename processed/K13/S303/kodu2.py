from turtle import *

def draw(num, length):
    speed(10)
    deg = 90 if num % 2 == 0 else -90
    forward(length)
    if num != 1: draw(num-1, length/2)
    right(deg)
    forward(length)
    if num != 1: draw(num-1, length/2)
    right(deg)
    forward(length)
    if num != 1: draw(num-1, length/2)
    right(deg)
    forward(length)
    right(deg)
    
draw(4, 200)