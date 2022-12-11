from turtle import *

def ruudud (tase, pikkus):
    if tase ==1:
        down()
        forward (pikkus)
        left (90)
        forward (pikkus)
        left (90)
        forward (pikkus)
        left (90)
        forward (pikkus)
        up ()
        return
    else:
        down ()
        forward (pikkus)
        pikkus = (pikkus/2)
        ruudud(tase-1, pikkus)
        pikkus = pikkus*2
        ruudud (tase, pikkus)
        up ()
print (ruudud(4, 100))
        