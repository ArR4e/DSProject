#2. Minu shuffle
from random import randint

def minu_shuffle(järjend):
    lagi=len(järjend)-1
    for el in järjend:
        juhuslik1=randint(0, lagi)
        juhuslik2=randint(0, lagi)
        järjend[juhuslik1], järjend[juhuslik2] = järjend[juhuslik2], järjend[juhuslik1]
        
        

#el = järjend[random.sample(range(len(järjend)), 1)[0]]
print(minu_shuffle([1, 2, 3, 4, 4, 5, 6, 1, 7]))