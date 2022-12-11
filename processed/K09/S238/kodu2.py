from random import *
def minu_shuffle(a):
    a.reverse()
    for i in range(len(a)):
        asendus = a.pop(i)
        suvanr = randint(0,len(a))
        a.insert(suvanr,asendus)
    print(a)

a = [1,2,3,4,5,6,7]

(minu_shuffle(a))