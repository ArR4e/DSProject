from turtle import *
speed(10)
def fraktaal(arv, külg):
    for i in range(3):
        forward(külg)
        
        if arv > 1:
            külg /= 2
            left(90)
            fraktaal(arv - 1, külg)
            right(90)
            külg *= 2
        right(90)
    
    forward(külg)
    right(90)            

exitonclick()