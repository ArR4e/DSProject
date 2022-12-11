from turtle import *



def fraktal(tase):
    global pikkus, pööre
    
    for i in range(3):
        forward(pikkus)
        
        if tase > 1:
            pikkus = pikkus/2
            pööre = -pööre
            fraktal(tase-1)
            pööre = -pööre
            pikkus = pikkus*2
        
        right(pööre)
    forward(pikkus)
    right(pööre)
        
pikkus=100
pööre = 90
fraktal(4)