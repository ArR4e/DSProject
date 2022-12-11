import random
def minu_shuffle(a):
    for i in a:
        i = len(a) - 1
        juhuslik = random.randint(0, i)
        juhuslik2 = random.randint(0, i)
        a[juhuslik], a[juhuslik2] = a[juhuslik2], a[juhuslik]
