from turtle import *
speed(0)
hideturtle()
    
def ruut(n,l=100):
    for i in range(3):
        forward(l)
        
        if n > 1:
            l = l/2
            color("red")
            ruut(n-1,l)
            color("blue")
            l = l*2
        
        left(90)
    forward(l)
    right(90)

ruut(4)