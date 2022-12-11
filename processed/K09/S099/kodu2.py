from random import randint

def minu_shuffle(jär):
    for i in range(0, len(jär)-1):
        e = randint(0, len(jär)-1)
        p = jär[i]
        jär[i] = jär[e]
        jär[e] = p
        
        
    
    