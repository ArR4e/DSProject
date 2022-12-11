from turtle import *  

def fraktal(tase, pikkus):
    if tase == 0:
       right(180)
    else:
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
        left(90)
        
speed(2)

        
    
        
        
    
        

        
        
    