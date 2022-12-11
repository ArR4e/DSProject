from turtle import*
import time

def ruudud(a):
    #time.sleep(1)
    if a > 1:
        for i in range(4):
            forward(25*a)          
            if i < 3:
                ruudud(a-1)
            left(90)
        left(180)
    elif a == 1:
        for i in range(4):
            forward(25)
            right(90)
    
    
    
ruudud(3)