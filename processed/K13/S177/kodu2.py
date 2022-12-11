from turtle import*
def fraktal(sügavus, pikkus):
    if sügavus == 0 or sügavus == 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        return
    else: 
        for i in range(sügavus+1):
            forward(pikkus)
            left(90)
            if i < sügavus:
                for i in range(sügavus + 1):
                    forward(pikkus/2)
                    left(90)
                    if i < sügavus:
                        for i in range(sügavus + 1):
                            forward (25)
                            left(90)
                            left(180)
                    left(180)
            left(180)
            
#ma ei osanud rekursiooniga teha
#         for i in range(sügavus+1):
#             fraktal(sügavus-1, pikkus/2)
#             if i < sügavus:
#                 for i in range(sügavus):
#                     fraktal(sügavus-1, pikkus/2)
#                     if i < sügavus:
#                         for i in range(sügavus):
#                             fraktal(sügavus-1, pikkus/2)
#                     left(180)
#                 left(180) 
    
fraktal(3, 100)    
    
