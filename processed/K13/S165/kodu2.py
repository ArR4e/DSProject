from turtle import *

suund = 90

def fraktal(pikkus, sügavus):
    global suund


    
    for i in range(3):
        forward(pikkus)
        
        
        if sügavus > 1:
            
            suund = -suund
            fraktal(pikkus /2,sügavus-1 )
            suund = -suund
            
        right(suund)
    
    forward(pikkus)
    right(suund)
    


exitonclick()










