from random import randint
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(a):
    b = 0
    for i in a:
        c = randint(0, len(a)-1)
        a[b], a[c] = a[c], a[b]
        b += 1
#    return(a)
#print(minu_shuffle(a))
        
