from turtle import*

def fraktal(a,sügavus):
    if sügavus>=1:
        for i in range(4):
            forward(a)
            left(90)
            if i < 3:
                fraktal(a*0.5,sügavus-1)
            left(180)           
    else:
        return

        
        
    