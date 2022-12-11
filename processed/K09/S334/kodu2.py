from random import randint
def minu_shuffle(mlist):
    n = len(mlist)
    for i in range(n):
        j = randint(0, n-1)
        element = mlist.pop(j)
        mlist.append(element)
        