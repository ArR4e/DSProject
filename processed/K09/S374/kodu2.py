from random import choice

def minu_shuffle(a):
    b = a[:]
    
    for i in range(len(a)):
        suvaline_arv = choice(b)
        a[i] = suvaline_arv
        b.remove(suvaline_arv)

