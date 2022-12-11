from turtle import *

def ruudud(sügavus):
    global k, kraad
    
    for i in range(3):
        forward(k)
        
        if sügavus >1:
            k /= 2
            kraad = - kraad
            ruudud(sügavus -1)
            kraad = - kraad
            k *= 2
            
        right(kraad)
        
    forward(k)
    right(kraad)
               
#k on kuljepikkus    
k = 100
kraad = 90
    
print(ruudud(5))