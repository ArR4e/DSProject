from turtle import *
speed(0)
wn = Screen()
wn.tracer(0)

def ruut(size, n=4):
    if n > 1:
        forward(size)
        right(90)
        ruut(size, n-1)
    elif n == 1:
        forward(size)
        
def fraktal(size, aste):
    if aste == 1:
        ruut(size)
    elif aste > 1:
        for i in range(3):
            forward(size)
            fraktal(size/2, aste-1)
        
        forward(size)
    

fraktal(300, 2)
wn.update()
wn.mainloop()

    