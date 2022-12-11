from turtle import*
def joonis(n, pikkus):
    forward(pikkus)
    if n>1:
        joonis(n-1, pikkus*0.5)
        forward(pikkus)
        joonis(n-1, pikkus*0.5)
        forward(pikkus)
        joonis(n-1, pikkus*0.5)
        forward(pikkus)
    if n==1:
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        
joonis(2,100)