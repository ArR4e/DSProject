from turtle import *
speed(0)
def fraktal(tase,pikkus):
    
    if tase==0:
        return 0
    
    else:
        for i in range(4):
            fd(pikkus)
            left(90)
            if i<3 :
                fraktal(tase-1,pikkus/2)
                
            left(180)
    
fraktal(3,100)


exitonclick()
        
