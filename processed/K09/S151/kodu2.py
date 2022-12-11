import random

a = [1, 3, 5, 6, 8, 9, 2, 4, 7]

def minu_shuffle(asi):  
    b = asi.copy()
    for i in range(0, len(asi)):
        asi[i] = random.choice(b)
        b.remove(asi[i])
    return asi

print(a)
print(minu_shuffle(a))