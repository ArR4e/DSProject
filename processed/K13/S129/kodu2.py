# fraKtalid
from turtle import *

def fraktal(tase):
    global pikkus, suund
    for _ in range(3):
        fd(pikkus)
        if tase > 1:
            pikkus = pikkus / 2
            suund = - suund
            fraktal(tase-1)
            suund = - suund
            pikkus = pikkus * 2
        
        right(suund)
    fd(pikkus)
    right(suund)
        
        
        
pikkus = 100
suund = 90

fraktal(4)

exitonclick()