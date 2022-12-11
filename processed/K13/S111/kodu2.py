from turtle import *

def ruut(külg,korrad):
    if korrad>=1:
        for i in range(4):
            forward(külg)
            right(90)
            if i<3:
                ruut(külg/2,korrad-2)
                right(180)
        right(180)
exitonclick()