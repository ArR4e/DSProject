from random import randint

def minu_shuffle(a):
    if a == []:
        return
    else:
        for k in range(100):
            i = randint(0, len(a)-1)
            x = a.pop(i)
            a.append(x)
            print(a)
        return

minu_shuffle([2, 5, 7, 1,3 , 7, 2, 8,4 ])
