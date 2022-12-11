import random

proovilist = [10, 20, 30 , 40]

def minu_shuffle(proovilist):
    for i in range(len(proovilist)-1, 0, -1):
        element = random.randint(0, i + 1)
        proovilist[i], proovilist[element] = proovilist[element], proovilist[i]
        
    return proovilist   
    
print(minu_shuffle(proovilist))