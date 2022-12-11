from turtle import *

def ruudud(aste,pikkus):
    if aste>1:
        for i in range(3):
            forward(pikkus)
            left(90)
            ruudud(aste-1,0.5*pikkus)
        forward(pikkus)
        left(90)
    elif aste==1:
        for i in range(4):
            forward(pikkus)  
            right(90)
        left(180)
    
        
        
        
ruudud(4,200)
    