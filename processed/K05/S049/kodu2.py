a = input("Sisesta sõne: ")

#https://www.geeksforgeeks.org/string-punctuation-in-python/
import string
b = string.punctuation

import random
c = str(random.choice(b))

List = list(a)
def suurväike(a):
    for x in range(0, len(a)):
        if a[x] in b:
            a[x] = c
        else:
            a[x] =  str.swapcase(a[x])
    a = "".join(a)
            
    return(a)


print(suurväike(List))