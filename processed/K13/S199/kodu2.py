from turtle import *

def fraktal(tase, pikkus):
    if tase == 0:
        return 
    else:
        fraktal(tase-1, pikkus*0.5)
        for i in range(3**(tase)):
            forward(2*pikkus)
            left(90)
            forward(pikkus)
            left(90)
            forward(pikkus)
            left(90)
            forward(pikkus)
        
fraktal(2, 100)            
exitonclick()
    

        