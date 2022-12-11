from statistics import harmonic_mean
import matplotlib.pyplot as plt
with open(input("Sisestage algandmete failinimi: ")) as aktsiad:
    sisu = aktsiad.readlines()
järjend = []
for i in range(len(sisu)):
    järjend += [float(sisu[i].strip().split(",")[1])]
n = int(input("Mitme elemendi kaupa soovite keskmistamist rakendada? "))
def silu_andmed(järjend,n):
    keskmendatud = []
    for i in range(len(järjend)):
        if i < n: keskmendatud += [harmonic_mean(järjend[:i+1])]
        elif i > n: keskmendatud += [harmonic_mean(järjend[i-n:i])]
    return keskmendatud
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylim(0,0.02)
ax.plot(list(range(0,len(järjend)-1)),silu_andmed(järjend,n),color="red")
ax.plot(list(range(0,len(järjend))),järjend)
plt.show()