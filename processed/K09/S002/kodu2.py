from random import randint

def minu_shuffle(lst):
    for i in range(len(lst)):
        rnd = randint(0,len(lst)-1)
        a = lst[i]
        lst[i] = lst[rnd]
        lst[rnd] = a

a = [1,2,3,4,5,6,7,8,9]
minu_shuffle(a)
print(a)
print(sorted(a))