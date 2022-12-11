import random
from string import *
import string
from os.path import *
def suurväike(a):
    g = a.swapcase()
    for i in g:
         if i in string.punctuation:
             k = [string.punctuation]
             g.replace(i, random.choice(k))
    print(g)
    
a = input("sisesta miskit: ")
print (suurväike(a))