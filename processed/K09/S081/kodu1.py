from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(j, n):
    jrnr = len(j)
    vastus = []
    vahep = []
    for a in range(jrnr):
        if a < n:
            for s in range(a+1):
                vahep.append(j[s])
            vastus.append(harmonic_mean(vahep))
            vahep.clear()
        else:
            for k in range(n):
            #sisend = harmonic_mean([j[a], j[a-1], j[a-2]])
                indikaator = a-k
                vahep.append(j[indikaator])
            vastus.append(harmonic_mean(vahep))
            vahep.clear()
    return vastus
                

algandmed = []

fnimi = input('Sisesta faili nimi: ')

fail = open(fnimi, encoding='UTF-8')

for rida in fail:
    nr = rida.strip('\n').split(',')[1]
    algandmed.append(float(nr))

fail.close()

silutud = silu_andmed(algandmed, 50)


fig = plt.figure()
plt.plot(algandmed)
plt.plot(silutud)
plt.show()




