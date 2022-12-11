from random import randint

def minu_shuffle(a):
    mitu = len(a)
    viimane_indeks = mitu - 1
    for i in a:
        indeks = randint(0, viimane_indeks)
        a.pop(indeks)
        a.insert(i, indeks)
print(minu_shuffle([1, 2, 3, 4]))