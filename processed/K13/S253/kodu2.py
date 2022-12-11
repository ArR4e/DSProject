from turtle import *

pikkus = 100
suund = 90   
def fraktalN(tase):
    global pikkus, suund
    for i in range(3):
        fd(pikkus)
        if tase > 1:
            pikkus /= 2
            suund = -suund
            fraktalN(tase-1)
            suund = -suund
            pikkus *= 2
        rt(suund)
    fd(pikkus)
    rt(suund)
speed(0)
fraktalN(3)