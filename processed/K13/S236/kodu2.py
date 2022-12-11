from turtle import *

def fraktal(n, pikkus):
    if n == 1:
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
    else:
        
        fraktal(n - 1, pikkus)
        left(90)
        fraktal(n - 1, pikkus/2)
        forward(pikkus)
        fraktal(n - 1, pikkus/2)
        forward(pikkus)
        fraktal(n - 1, pikkus/2)
        back(pikkus/2)
        right(90)




left(90)
fraktal(2, 100)
exitonclick()

#ei saa korralikult debugida sellist ülesannet ja mõte jooksis kokku:D