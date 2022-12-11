from turtle import *

def ruudud(suurus, sügavus):
    if sügavus>0:
        for i in range(4):
            forward(suurus)
            left(90)
            if i<3:
                ruudud(suurus*0.5, sügavus-1)
            left(180)

#ruudud(100,5)
exitonclick( )