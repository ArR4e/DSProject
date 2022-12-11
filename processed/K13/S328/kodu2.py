from turtle import *

l = 200
d = 90

def kilpkonn(n):
    global l, d

    for i in range(3):
        forward(l)
        if n > 1:
            l /= 2
            d = - d
            kilpkonn(n - 1)
            d = - d
            l *= 2
        right(d)
            
    forward(l)
    right(d)
        
    
kilpkonn(3)