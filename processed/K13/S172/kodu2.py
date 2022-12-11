from turtle import *

def frak(tase, kulg):
    if tase == 0:
        return True
    elif tase == 1:
        forward(kulg)
        left(90)
        frak(tase, kulg)
        left(180)
    else:
        forward(kulg)
        left(90)
        frak(tase, kulg)
        left(180)
        return frak(tase-1, kulg*0.5)

