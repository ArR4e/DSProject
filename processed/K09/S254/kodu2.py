from random import *

def minu_shuffle(järjend):
    for indeks in range(len(järjend)):
        juhuslik_arv = randint(0,len(järjend)-1)
        juhuslik_arv2 = randint(0,len(järjend)-1)
        järjend[juhuslik_arv2], järjend[juhuslik_arv] = järjend[juhuslik_arv], järjend[juhuslik_arv2]
    
    
    
    
järjend = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(minu_shuffle(järjend))