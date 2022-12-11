import turtle as kp
esimene = 0
def fraktal(suurus,tase):
    global esimene
    if tase %2 == 1 and esimene == 0:
        esimene = 1
        kp.right(90)
    else:
        esimene = 2
    if tase >= 1:
        if tase %2 == 1:    
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.left(90)
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.left(90)
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.left(90)
            kp.forward(suurus)
            kp.left(90)
        if tase %2 == 0 :
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.right(90)
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.right(90)
            kp.forward(suurus)
            fraktal(suurus*0.5,tase-1)
            kp.right(90)
            kp.forward(suurus)
            kp.right(90)
a,b = 30,3        
fraktal(a,b)
kp.exitonclick()