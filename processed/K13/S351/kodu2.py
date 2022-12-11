from turtle import *
def fraktali_joonistamine(sügavus):
    global pikkus, nurk
    for i in range(3):
        forward(pikkus)
        
        if sügavus>1:
            pikkus/=2
            nurk=(-nurk)
            fraktali_joonistamine(sügavus-1)
            nurk=(-nurk)
            pikkus=pikkus*2
        right(nurk)
    forward(pikkus)
    right(nurk)
    
pikkus=100
nurk=90
fraktali_joonistamine(2)
exitonclick()

