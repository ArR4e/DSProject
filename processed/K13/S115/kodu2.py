from turtle import*

def fraktal (tase, pikkus):
    if tase >= 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        right(90)
        fraktal(tase-1, pikkus * 0.5)
        right(90)
        fraktal(tase-1, pikkus *0.5)
        

        
left(90)
fraktal(2,100)