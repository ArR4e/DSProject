a = list(map(int, input('Sisestage arvud: ').split(' ')))
    
def minu_shuffle(a):
    from random import randint, sample
    suva = sample(a, len(a))

    for i in range(len(a)):
        a[i] = suva[i]
