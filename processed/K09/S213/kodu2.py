from random import randint

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]

def minu_shuffle(a):

    for i in range(0, len(a)):
        
        algne_list = []
        for el in a:
            algne_list.append(el)
        
        x = randint(0, len(a) - 1)
        
        algne = algne_list[i]
        vahetus = algne_list[x]
        
        a[i] = vahetus
        a[x] = algne