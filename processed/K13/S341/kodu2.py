from turtle import *
def fact(n):
    if n == 0:
        return 1
    if n > 0:
        return fact(n-1) * n

for i in range(4):
    fact(4)
    forward(100)
    left(90)
    if i < 3:
        for i in range(4):
            fact(4)
            forward(50)
            left(90)
            if i < 3:
                for i in range(4):
                    fact(4)
                    forward(25)
                    left(90)
                    left(180)
            left(180)
    left(180)
    