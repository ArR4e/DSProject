from random import*

def minu_shuffle(a):
    if a == []:
        return
    b = list(range(0,len(a)))
    for i in range(0, 100):
        a.insert(0, a.pop(choice(b)))

print(minu_shuffle([1,2,3,4,5,6,7,8,9]))