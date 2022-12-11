import random

def minu_shuffle(a):
    i=0
    lamplist = []
    m= 0
    while True:
        m = random.choice(a)
        if m not in lamplist:
            a[random.randint(0, len(a)-1)] = m
            i +=1
            lamplist.append(m)
        if i > len(a):
            break

a = [1, 2, 3, 4, 5, 6, 7]
minu_shuffle(a)
print(a)

