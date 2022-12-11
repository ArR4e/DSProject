from random import randint

def minu_shuffle(a):
    for i in range(len(a)):
        temp = a.pop(i)
        a.insert(randint(0, len(a)), temp)
    #return a