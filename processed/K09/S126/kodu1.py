import mathplotlib.pyplot as plt 

fail = open("aktsiadtest.txt", "r")
import

aktsiad = []
def silu_andmed(järjend):
    hinnad = []
    sisu = []
    kuupäevad = []
    faili_sisu = fail.readlines()
    for i in range(len(faili_sisu)):
        rida = (faili_sisu[i]).strip().split(",")
        sisu.append(rida)
        
    for i in range(len(sisu)):
        hind = sisu[i][1]
        kuupäev = sisu[i][0]
        hinnad.append(float(hind))
        kuupäevad.append(kuupäev)
    return(hinnad, kuupäevad)

a = max(silu_andmed(fail)[0])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(silu_andmed(fail)[1], silu_andmed(fail)[0], "o-", label="hinnad")
ax.set_ylim(0.001, a)
ax.legend()
plt.show()