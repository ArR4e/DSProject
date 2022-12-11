from statistics import harmonic_mean
def silu_andmed(algandmed, täisarv):
    uued_andmed = []
    H = [] # Harmoonilise keskmine arvutamiseks
    j = 1 # järjekorranumber
    i = 0 # järjendi järgmise elemendi kättesaamiseks
    for element in algandmed:
        if j <= täisarv:
            H.append(element)
            uued_andmed.append(harmonic_mean(H))
            j += 1
        elif j > täisarv:
            H.pop(0)
            H.append(algandmed[i+täisarv])
            uued_andmed.append(harmonic_mean(H))
            i += 1
    return uued_andmed

import matplotlib.pyplot as plt

fail = input('Sisesta failinimi: ')
r = open(fail, 'r')
andmed = [] # Siia tulevad failist saadud hinnad igalt realt
andmete_arv = [] # Teisisõnu ridade arv failis
i = 1 # Et muutujasse 'andmete_arv' lisada järjendisse uus n-ö järjekorranumber ehk mitmenda reaga tegu on tsüklis
for read in r:
    read = read.strip().split(',')
    hind = float(read[1])
    andmed.append(hind)
    andmete_arv.append(i)
    i += 1
    
harm_k = silu_andmed(andmed, 50) # Eeldades, et n = 50
r.close()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmete_arv, andmed)
ax.plot(andmete_arv, harm_k)
plt.show()
    