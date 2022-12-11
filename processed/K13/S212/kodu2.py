from turtle import *

        
def ruudud(pikkus, depth, algnedepth):
    for i in range(3):
        forward(pikkus)
        if depth != 1:
            ruudud(int(pikkus/2), depth-1, algnedepth)
        if (algnedepth - depth) % 2 == 0:
            right(90)
        else:
            left(90)
    forward(pikkus)
    if (algnedepth - depth) % 2 == 0:
        right(90)
    else:
        left(90)
    
ruudud(100, 4, 4)

exitonclick()
    
    
    