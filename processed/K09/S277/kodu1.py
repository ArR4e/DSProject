from statistics import harmonic_mean
import matplotlib.pyplot as plt

fnimi = input('Sisestage faili nimi: ')
n = int(input('Sisestage täisarv: '))
f = open(fnimi, 'r', encoding = 'utf-8')
read = f.read().split('\n')

def silu_andmed(alg, n):
    uus = []
    while True:
        indeks = 1
        while indeks < n:
            if len(uus) == len(nr):
                break
            uus = uus + [harmonic_mean(alg[:indeks])]
            indeks += 1
        if indeks == n:
            while indeks <= len(alg):
                uus = uus + [harmonic_mean(alg[indeks - n:indeks])]
                indeks += 1
        break
    return uus  
if read == ['']:
    print('Antud andmete hulk on tühi!')
else:
    nr = []
    alg = []
    
    for i in range(len(read)):
        nr = nr + [i]
        
    for rida in read:
        alg = alg + [float(rida.split(', ')[1])] 

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(nr, alg, label = 'algsed andmed')
    ax.plot(nr, silu_andmed(alg, n), label = 'silutud andmed')

    plt.show()
