import random
import copy

def minu_shuffle(a):
    b = copy.copy(a)
    i = 0
    while i < (len(a)):
        indeks = random.randint(0, len(a)-1)
        arv = a.pop(indeks)
        a.append(arv)
        i += 1
    
a = []        
minu_shuffle(a)
print(a)