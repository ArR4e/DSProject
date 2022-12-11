from random import randint

def minu_shuffle(list):
    for n in range(randint(100,1001)):
        if len(list) == 0:
            break
        arv = list.pop(randint(0,len(list)-1))
        list.append(arv)

