from turtle import*
def ruudud(n):
    global nurk
    global pikkus
    for i in range(3):
        forward(pikkus)
        if n > 1:
            nurk = -nurk
            pikkus /= 2
            ruudud(n-1)
            nurk = -nurk
            pikkus *= 2
        right(nurk)
    forward(pikkus)
    right(nurk)
pikkus = 50
nurk = 90
ruudud(4)
        