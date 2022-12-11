import random
def minu_shuffle(a):
    for i in range(0, len(a)+1):
        if a == []:
           break
        el = random.choice(a)
        ind = a.index(el)
        el2 = random.choice(a)
        ind2 = a.index(el2)
        a[ind], a[ind2] = a[ind2], a[ind]
    print(a)
