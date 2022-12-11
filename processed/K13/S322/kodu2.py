from turtle import *

def ruudud(suurus, hulk):
    if hulk > 0:
        # for tsükkel käivitab lihtsalt neid käsklusi
        # kolm korda (et vältida sama asja kirjutamist)
        for i in range(3):
            # joonista külg
            forward(suurus)
            right(90)
            # muuda suurus negatiivseks (et kilpkonn liiguks
            # kujundist välja, mitte selle sisse)
            ruudud(-suurus/2, hulk-1)
        # joonista külg ilma rekursioonita
        forward(suurus)
        right(90)

#speed(-1)
#delay(0)
#ruudud(120, 4)
#exitonclick()