from turtle import*

def fraktal(tase, pikkus):
    for a in range(3):
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus * 3)
    fraktal(tase-1, pikkus/2)
    
    
    
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)   
fraktal(2, 50)
exitonclick()