import random

def minu_shuffle(a):
    i = 0
    while i < len(a):
        if len(a) < 2:
            x = a.pop(0)
            a.insert(random.randint(0,len(a)), x)
            i += 1
            
        else:
            x = a.pop(random.randint(1, len(a)-1))
            a.insert(random.randint(0,len(a)), x)
            i += 1
            
        
    print(a)
    
minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])