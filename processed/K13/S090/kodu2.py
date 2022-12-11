import turtle
pikk = 100

def fraktal(x, tob, turn_direction= 2):
    global pikk
    if x == 1:
        tob.forward(pikk)
        tob.left(90)
        tob.forward(pikk)
        tob.left(90)
        tob.forward(pikk)
        tob.left(90)
        tob.forward(pikk)
        return
    else:
        tob.forward(pikk)
        pikk = pikk / 2
        fraktal(x - 1, tob)
        pikk = pikk * 2
        if turn_direction == 0:
            tob.forward(pikk)
            return
        fraktal(x, tob, turn_direction=turn_direction - 1)
        
tur_ob = turtle.Turtle()
fraktal(4, tur_ob)
        
