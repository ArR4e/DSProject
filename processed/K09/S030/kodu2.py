import random
def minu_shuffle(lst1):
    n=len(lst1)
    for i in range(n):
        m=random.randint(0,n-1)
        el=lst1.pop(m)
        lst1.append(el)
    print(lst1)
