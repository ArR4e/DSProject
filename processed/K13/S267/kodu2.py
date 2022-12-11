from turtle import *

def ruudud(tase):
    global kylg, suund
    
    for i in range(3):
        forward(kylg)
        
        if tase > 1:
            kylg = kylg / 2
            suund = - suund
            ruudud(tase - 1)
            kylg = kylg * 2
            suund = - suund
        right(suund)
        
    forward(kylg)
    right(suund)

kylg = 100
suund = 90
        
ruudud(4)

exitonclick()