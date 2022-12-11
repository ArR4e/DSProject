from turtle import *

def äge(korduste_arv, suurus):
    if korduste_arv == 1:
        for i in range(4):
            forward(suurus)
            left(90)
            left(180)
    elif korduste_arv > 1:
        for i in range(4):
            forward(suurus)
            left(90)
            if i < 3:
                äge(korduste_arv-1,suurus*0.5)
            left(180)

speed(10000)
äge(4,100)
exitonclick()
