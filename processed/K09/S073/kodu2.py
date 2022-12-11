import random
def minu_shuffle(l):
    order = random.sample(range(len(l)), len(l))
    newlist = list()
    for i in range(len(l)):
        newlist.append(l[order[i]])

    for i in range(len(l)):
        l[i] = newlist[i]