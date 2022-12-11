import turtle

def joonistus(tase, pikkus):
    if tase == 0:
        return
    else:
        for i in range(4):
            turtle.forward(pikkus)
            turtle.left(90)
            if i < 3:
                if tase == 1:
                    turtle.left(180)
                return joonistus(tase - 1, pikkus * 0.5)
joonistus(4, 100)
                
            
                