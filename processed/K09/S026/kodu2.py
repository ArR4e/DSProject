from random import randint

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(järjend):
    for arv in a:
        juhuslik = randint(arv.pop(randint))
        print(juhuslik)
        
minu_shuffle(a)