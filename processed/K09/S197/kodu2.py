from random import randint
def minu_shuffle(a):
    for i in range(len(a)):
        a.append(a.pop(randint(0, len(a) - (i+1))))