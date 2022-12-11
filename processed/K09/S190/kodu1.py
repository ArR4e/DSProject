from statistics import harmonic_mean
import matplotlib.pyplot as plt

# andmete eraldamine failist järjenditesse
faili_nimi = input("Sisesta faili nimi: ")
fail = open(faili_nimi)
algandmed = []
for rida in fail:
    elementide_järjend = rida.split(", ")
    hind = float(elementide_järjend[-1])
    kuupäev = elementide_järjend[0]
    algandmed.append(hind)            

def silu_andmed(algandmed,elementide_arv): 
    # hindade silumine
    keskmiste_järjend = []
    for i in range(len(algandmed)):
        algus = max(0,i+1-elementide_arv)
        vahemik = algandmed[algus:i+1]
        keskmine = float(harmonic_mean(vahemik))
        keskmiste_järjend.append(keskmine)
    return keskmiste_järjend

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(algandmed, "r", label = "alghinnad")
ax.plot(silu_andmed(algandmed,50), "-g", label = "keskmistatud hinnad")
plt.show()
   