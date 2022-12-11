from random import randint

def minu_shuffle(a):
    for i in range(len(a) - 1, 0, -1):
        juhuslik = randint(0, i)
        a[i], a[juhuslik] = a[juhuslik], a[i]

a = input("Sisestage oma järjend: ").split()
