from turtle import *

def fraktal(n, küljepikkus):
    
    for i in range(3):        
        if n == 0:
            return
        fd(küljepikkus)
        
        if n > 1:
            fraktal(n-1, küljepikkus/2)                
        
        left(90)
        
    fd(küljepikkus)
    right(90)

fraktal(3, 100)
exitonclick()        