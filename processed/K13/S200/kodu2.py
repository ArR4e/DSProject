from turtle import*

def fraktal(sügavus,külg):
        if sügavus >= 1:
            for i in range(4):
                forward(külg)
                left(90)
                if i < 3:
                    fraktal(sügavus-1,külg/2)
                left(180)
        
        elif sügavus == 0:
            return()
