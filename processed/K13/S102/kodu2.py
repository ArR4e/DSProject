from turtle import*
speed(0)
def fraktal(pikkus, aste):
    #pikkus=80
    if aste!=0:
        for i in range(3):
            forward(pikkus)
            fraktal(pikkus*0.4, aste-1)
        forward(pikkus)
    else:
        left(90)

            
fraktal(80, 5)
exitonclick()
    