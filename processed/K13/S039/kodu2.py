from turtle import*

def ruut(k):  
    forward(k)
    left(90)
    forward(k)
    left(90)
    forward(k)
    left(90)
    forward(k)
    

def fraktal(k,sügavus):
        if sügavus>1:
            for i in range(3):
                forward(k)
                
                fraktal(k/2,sügavus-1)
            forward(k)
        else:
            ruut(k)
        
fraktal(40,3)