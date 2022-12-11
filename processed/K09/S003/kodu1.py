import matplotlib.pyplot as plt

def silu_andmed(järjend, arv):
    uusjärjend = []
    from statistics import harmonic_mean
    for i in range(len(järjend)):
        if i < arv:
            esimene = 0
        else:
            esimene = i-arv+1
        uusjärjend.append(harmonic_mean(järjend[esimene:i+1]))
    return uusjärjend

failinimi = input("palun sisesta failinimi: ")
fail = open(failinimi)
kuupäevad = []
hinnad = []
for rida in fail:
    reajärjend = rida.strip("\n").split(",")
    kuupäevad.append(reajärjend[0])
    hinnad.append(float(reajärjend[1]))
    
for i in range(len(kuupäevad)):
    
    kuupäevad[i]= i
    
silutudhinnad = silu_andmed(hinnad,3)
plt.plot(kuupäevad, hinnad, silutudhinnad)
plt.xlabel("Kuupäevad")

plt.show()
