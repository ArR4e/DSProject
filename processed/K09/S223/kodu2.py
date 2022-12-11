import random
def minu_shuffle(list_random):
    length = len(list_random)-1
    if list_random != []:
        for x in range(100):
            a = random.randint(0,length)
            b = random.randint(0,length)
            list_random[a], list_random[b] = list_random[b], list_random[a]
