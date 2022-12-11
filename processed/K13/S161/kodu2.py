from turtle import*
def ruudud(x,y):
    if x==0:
        return done()
    else:
        for i in range(4):
            forward(y)
            left(90)
            if i < 3:
                for i in range(4):
                    forward(y/2)
                    left(90)
                    left(180)
            left(180)
        left(180)
        return ruudud(x-1,y/2)
ruudud(4,300)