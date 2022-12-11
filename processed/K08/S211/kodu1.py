from random import sample

def bingo():
    
    jrj1 = sample(range(1,11), 3)
    jrj2 = sample(range(11, 21), 2)
    
    while True:
        
        if 1 in jrj1 and 2 in jrj1 and 3 in jrj1:
            jrj1=sample(range(1,11), 3)
        else:
            break
        
        for el in jrj1:
            if (el in jrj2):
                jrj1 = sample(range(1,11), 3)
            else:
                break
    
    
    lõplik = jrj1+jrj2
        
    return(lõplik)
    
print(bingo())