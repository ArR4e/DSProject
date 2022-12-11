from random import randint#,seed
#seed(11)
def minu_shuffle(l):
    for i in range(len(l)):
        a = l[i]
        c = randint(0,len(l)-1)
        b = l[c]
        l[i] = b
        l[c] = a
#minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6])
