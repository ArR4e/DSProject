def minu_shuffle(a):
    from random import choice
    ennik = tuple(a)
    indeksid = []
    for i in range(len(a)):
        indeksid.append(i)
    indeks = -1
    for i in range(0, len(ennik)):
        while indeks == -1:
            indeks = choice(indeksid)
        a[i] = ennik[indeks]
        indeksid[indeks] = -1
        indeks = -1
        
        
        