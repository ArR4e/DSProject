from turtle import *
def sarnased_ruudud(pikkus,tase):
    if tase>=1:
        if tase%2==0:
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            right(90)
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            right(90)
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            right(90)
            forward(pikkus)
            right(90)
        elif tase%2==1:
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            left(90)
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            left(90)
            forward(pikkus)
            sarnased_ruudud(pikkus*0.5,tase-1)
            left(90)
            forward(pikkus)
            left(90)

exitonclick()