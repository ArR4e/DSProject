from turtle import*

# def sügavus(külg, arv):    
#     if arv == 1:
#         for i in range(4):
#             forward(külg)
#             right(90)
#             right(180)
#         return
#     else:
#         forward(külg)
#         right(90)
#         #left(180)
#         külg = külg/2
#         arv -= 1
#         #for i in range(1):
#         #    sügavus(külg, arv)
#         sügavus(külg, arv)
#         right(180)
#         külg = külg*2
#         forward(külg)
#         külg = külg/2
#         sügavus(külg, arv)
#         #return sügavus(külg, arv)
# sügavus(100, 2)

speed(200)

def sügavus(külg, arv, nurk):
    color("red")
    begin_fill()
    for i in range(3):
        forward(külg)
        
        if arv > 1:
            külg = külg / 2
            nurk = -nurk
            sügavus(külg, arv - 1,  nurk)
            nurk = -nurk
            külg = külg * 2
        
        right(nurk)

        
    forward(külg)
    end_fill()
    right(nurk)
    color("green")
    begin_fill()
    end_fill()
    
sügavus(100, 4, 90)