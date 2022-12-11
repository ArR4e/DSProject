import random
def minu_shuffle(lst):
    for el in range(len(lst)):
        randindex = random.randint(0,len(lst)-1)
        num = lst[randindex]
        lst[randindex] = lst[el]
        lst[el] = num