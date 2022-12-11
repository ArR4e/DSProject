from turtle import *

def ruudu_fraktal(n, küljepikkus):
    if n < 1:
        return 0
    else:
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        right(90)
        ruudu_fraktal(n-1, küljepikkus * 0.5)
#         forward(küljepikkus)
#         right(90)
#         ruudu_fraktal(n, küljepikkus)
    
ruudu_fraktal(3, 100)
exitonclick()