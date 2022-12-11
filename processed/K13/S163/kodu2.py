# Sarnaste ruutude fraktal
from turtle import *
speed(0)

def rek(tase, x):
    for i in range(4): 
        forward(x)
                     
        if tase > 1:
            if i < 3:
                rek(tase-1, 0.5*x)
      
        if tase % 2 == 0:
            left(90)
        else:
            right(90)
                         
rek(4, 100)