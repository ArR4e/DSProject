from random import randint

def minu_shuffle(a):
    kontroll = []
    b = a[:]
    a.clear()
    for i in range(0, len(b)):
        while True:
            param = randint(0,len(b)-1)
            if param not in kontroll:
                a.append(b[param])
                kontroll += [param]
                break
        