from random import randint

def minu_shuffle(a):
    for i in range(len(a)):
        if len(a) == 1:
            break
        else:
            a.insert(randint(0, len(a)-1), a.pop(randint(0, len(a)-1)))