from random import choice

def minu_shuffle(a):
    if len(a) > 1:
        for i in range(2 * len(a) + 1):
            el = choice(a[:-1])
            a.append(el)
            a.remove(el)
