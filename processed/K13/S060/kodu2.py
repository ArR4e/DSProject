from turtle import *
def fraktaal(tase,pikkus):
    if tase>=1:
        right(90)
        forward(pikkus)
        fraktaal(tase-1,pikkus*0.5)
        left(90)
        forward(pikkus)
        fraktaal(tase-1,pikkus*0.5)
        left(90)
        forward(pikkus)
        fraktaal(tase-1,pikkus*0.5)
        left(90)
        forward(pikkus)
        left(180)
fraktaal(4,100)
