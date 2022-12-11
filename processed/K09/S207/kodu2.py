from random import randint

def minu_shuffle(a):
    for i in range(0,(len(a)*3)):
        suv1 = randint(0,len(a)-1)
        suv2 = randint(0,len(a)-1)
        while suv1 == suv2:
            suv2 = randint(0,len(a)-1)
        a[suv1], a[suv2] = a[suv2], a[suv1]