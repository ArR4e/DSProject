from turtle import*

def fraktal(tase):
    global pikkus, suund
    for i in range(3):
        forward(pikkus)
        
        if tase > 1:
            pikkus = pikkus /2
            suund = -suund
            fraktal(tase-1)
            suund = -suund
            pikkus = pikkus*2
        
        right(suund)
        
    forward(pikkus)
    right(suund)

            

            
    
suund = 90
pikkus = 100
#speed("fastest")
fraktal(2)

exitonclick()
        
    