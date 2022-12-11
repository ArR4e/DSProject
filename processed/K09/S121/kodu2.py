import random

def minu_shuffle(_list):
    for i in range(0, len(_list)-1):
        rand = random.randint(0, i)
        _list[i], _list[rand] = _list[rand], _list[i]
    print(_list)
    
minu_shuffle([1, 5, 6, 8, 9, 7, 3, 4, 9])
