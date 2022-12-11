from random import randrange
def minu_shuffle(x):
    index = 0
    for arv in x:
        a = randrange(len(x)-1)
        x[index], x[a] = x[a], x[index]
        index += 1
    
minu_shuffle([3,1,2,3,1,4])    