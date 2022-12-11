from turtle import *
def fraktal(tase):
    if tase == 1:
        for i in range(4):
                forward(100)
                left(90)
    elif tase > 1:
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
                            left(180)
                    left(180)
            tase-=1
            left(180)
#     if tase >1:
#         forward(tase *100)
#         left(90)
#         forward(tase *100)
#         left(90)
#         forward(tase *100)
#         left(90)
#         forward(tase *100)
#         left(90)
#         fraktal(tase-1)
#         right(90)
#         fraktal(tase-1)
#         left(90)
#         backward(tase*100)
#     else:
#         return
fraktal(2)
    
