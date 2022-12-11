a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
from random import randint
from copy import deepcopy
def minu_shuffle(x):
    t=randint(0,len(a))
    y=deepcopy(x)
    for i in x:
        if t >= len(a):
            t=t-len(a)
            y.pop(t)
            y.insert(t,i)
            t+=1
        else:
            y.pop(t)
            y.insert(t,i)
            t+=1

    a.clear()
    for i in y:
        a.append(i)
    
#print(minu_shuffle(a))