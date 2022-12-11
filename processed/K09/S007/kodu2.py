from random import randint

def minu_shuffle(x):
    for i in range(len(x)):
        juhuslik_indeks = randint(0, len(x)-1)
        element = x[i]
        x[i] = x[juhuslik_indeks]
        x[juhuslik_indeks] = element
    
    
   
