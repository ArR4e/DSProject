from random import shuffle, randint

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def minu_shuffle(a):
    for i in range(len(a)):
        try:
            juhuslik = randint(0, len(a)-1)
            a[i], a[juhuslik] = a[juhuslik], a[i]
        except:
            break
            
minu_shuffle(a)
print(a)