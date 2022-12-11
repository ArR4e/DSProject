from random import randint

def minu_shuffle(mingi_list):
    pikkus = len(mingi_list)
    for i in range(pikkus):
        j = randint(0, pikkus-1)
        element = (mingi_list).pop(j)
        mingi_list.append(element)