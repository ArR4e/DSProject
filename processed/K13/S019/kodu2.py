import turtle 

def ruudud(n, külg):
    if n == 0:
        return n
    elif n == 1:
        for i in range(4):
            turtle.forward(külg)
            turtle.left(90)
            turtle.left(180)
#     elif n == 3:
#         for i in range(4):
#             turtle.forward(100)
#             turtle.left(90)
#             if i < 3:
#                 for i in range(4):
#                     turtle.forward(50)
#                     turtle.left(90)
#                     if i < 3:
#                         for i in range(4):
#                             turtle.forward(25)
#                             turtle.left(90)
#                             turtle.left(180)
#                     turtle.left(180)
#             turtle.left(180)
    else:
        ruudud(n-1,külg)
        m = külg
        for i in range(4):
            turtle.forward(külg)
            turtle.left(90)
            if i < 3:
                m = m/2
                for i in range(4):
                    turtle.forward(m)
                    turtle.left(90)
                    turtle.left(180)
            turtle.left(180)
        #turtle.left(180)
#ma ei oska :((
         