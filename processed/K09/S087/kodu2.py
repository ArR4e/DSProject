from random import randint

def minu_shuffle(test):
    n = len(test)
    
    for i in range(n):
        j = randint(i, n - 1)
        test[i], test[j] = test[j], test[i]
    
