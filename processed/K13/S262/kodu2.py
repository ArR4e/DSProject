from turtle import *
def ruudud(suurus,sygavus):
    if sygavus == 1:
        forward(suurus)
        left(90)
        forward(suurus)
        left(90)
        forward(suurus)
        left(90)
        forward(suurus)
        return
    else:
        forward(suurus)
        ruudud(suurus/2,sygavus-1)
        forward(suurus)
        ruudud(suurus/2,sygavus-1)
        forward(suurus)
        ruudud(suurus/2,sygavus-1)
        forward(suurus)
        return
ruudud(200,4)