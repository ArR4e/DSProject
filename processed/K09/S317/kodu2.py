import random
def minu_shuffle(a):
    for i in range (0, len(a)+1):
        if a == []:
            break
        indeks = random.choice(a)
        indeks = a.index(indeks)
        indeks2 = random.choice(a)
        indeks2 = a.index(indeks2)
        a[indeks], a[indeks2] = a[indeks2], a[indeks]
    print(a)