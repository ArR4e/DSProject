# 2. minu_shuffle

from random import randint

def minu_shuffle(järjend):
    for el in range(len(järjend)-1, 0, -1):
        i = randint(0, el)
        järjend[el], järjend[i] = järjend[i], järjend[el]
        #return(järjend)

#a = [2, 3, 5, 6, 7, 8]
#minu_shuffle(a)
#print(järjend)
        