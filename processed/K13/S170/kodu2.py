from turtle import *


def ruudud(sügavus):
    if sügavus == 1:
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        return
    if sügavus == 2:
        forward(100)
        ruudud(sügavus - 1)
        forward(100)
        ruudud(sügavus - 1)
        forward(100)
        ruudud(sügavus - 1)
        forward(100)
        
    if sügavus == 3:
        forward(150)
        ruudud(sügavus - 1)
        
        
    exitonclick()
    
right(90)
ruudud(2) #tehtud on kuni 2. sügavuseni