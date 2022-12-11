import random
def minu_shuffle(suvaline):
    k=len(suvaline)
    for i in range(0,k-1,2):
        muu=random.randint(0,k-1)
        suvaline[i], suvaline [muu] = suvaline [muu], suvaline[i]
    
        

