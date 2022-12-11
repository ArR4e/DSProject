from turtle import *

def ruut(külg,sügavus):
    if sügavus == 1 :
        forward(külg)
        right(90)
        forward(külg)
        right(90)
        forward(külg)
        right(90)
        forward(külg)
        right(90)
    else:
        forward(külg)
        ruut(külg*0.5,sügavus-1)
        left(90)
        forward(külg)
        ruut(külg*0.5,sügavus-1)
        left(90)
        forward(külg)
        ruut(külg*0.5,sügavus-1)
        left(90)
        forward(külg)
        left(90)
    
        
    
    