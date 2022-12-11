from turtle import *
#https://stackoverflow.com/questions/59009062/generating-square-fractals-with-python
def fraktal(sügavus, pikkus, suund=90):
    speed('fastest')
    for i in range(3):
        forward(pikkus)
        
        if sügavus > 1:
            fraktal(sügavus - 1, pikkus/2, -suund)

        right(suund)
        
    forward(pikkus)
    right(suund)
        
        

#print(fraktal(4, 100))
    
