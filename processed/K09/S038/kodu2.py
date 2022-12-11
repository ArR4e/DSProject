import random

test = [1,3,3,4,5,5,5,6,6]

def minu_shuffle(a):
    n = len(a)
    a = random.sample(a,n)
    
print(minu_shuffle(test))