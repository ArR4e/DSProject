def minu_shuffle(a):
    import random
    import copy
    b=copy.deepcopy(a)
    for i in range(0, len(a)):
        arv=random.choice(b)
        b.remove(arv)
        a[i]=arv



