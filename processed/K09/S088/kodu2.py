from random import randint

def minu_shuffle(a):
    count = len(a)-1
    for i in range(len(a)):
        element = a.pop(randint(0,count))
        count -= 1
        a.append(element)