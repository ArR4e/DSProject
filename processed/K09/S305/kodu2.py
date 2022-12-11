import random
def minu_shuffle(a):
    r = []
    while len(a) > 0:
        i = random.randrange(0, len(a))
        r.append(a.pop(i))
    a = r