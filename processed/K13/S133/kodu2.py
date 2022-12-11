from turtle import *

def fraktal(a):
    if a==1:
        for v in range(4):
            right(90)
            forward(100/a)
    else:
        n=(100/(a-1))
        s=3**(a-2)
        b=1
        j=a-1
        while s>0:
            if s>0:
                for v in range(4):
                    if v<3 and a>1:
                        if a>1:
                            penup()
                            forward(n)
                            pendown()
                        for i in range(4):
                            forward(100/a)
                            if i<3:
                                left(90)
            penup()
            forward(n)
            if a-j>0 and a==3:
                forward(100/(1))
            elif  a-j>0 and a==4 and s%3==0 and s%9!=0:
                forward(200)
                right(90)
            elif  a-j>0 and a==4 and (s%3!=0 or  s%9==0):
                forward(100/(2))
            pendown()
            s-=1
        if a-1>1:
            left(180)
        fraktal(a-1)
fraktal(4)
