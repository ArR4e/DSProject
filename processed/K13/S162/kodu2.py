from turtle import *
def fraktal(külg,tase):
    if tase>=1:
        for i in range(4):
            forward(külg)
            left(90)
            if i<3:
                fraktal(külg*0.5,tase-1)
            left(180)
        
        
        
fraktal(100,2)
