from turtle import *

for i in range(4):
    forward(100)
    left(90)
    if i < 3:
        for i in range(4):
            forward(50)
            left(90)
            if i < 3:
                for i in range(4):
                    forward(25)
                    left(90)
                    if i < 3:
                        for i in range(4):
                            forward(12.5)
                            left(90)
                            left(180)
                    left(180)
            left(180)
    left(180)
