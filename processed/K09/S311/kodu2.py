from random import randint
def minu_shuffle(a):
    for i in range(len(a)):
        suv = randint(0, len(a)-1)
        a[i], a[suv]  = a[suv], a[i]
    print(a)
a= [8,22,19,1,100]
minu_shuffle(a)