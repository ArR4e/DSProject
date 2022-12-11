from random import randint

def minu_shuffle(a):
    for i in range(len(a)):
        index = randint(0,len(a)-1)
        a.append(a[index])
        a.pop(index)