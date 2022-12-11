import turtle as t

def rfraktal(mitu):
    global pikkus, suund

    for i in range(3):
        t.forward(pikkus)
        
        if mitu > 1:
            pikkus /= 2
            suund = -suund
            rfraktal(mitu - 1)
            suund = -suund
            pikkus *= 2
            
        t.right(suund)
        
    t.forward(pikkus)
    t.right(suund)
    
pikkus = 100
suund = 90
            