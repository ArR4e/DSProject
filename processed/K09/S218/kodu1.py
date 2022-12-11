from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, arv):
    n=0
    i = 1
    pikkus = len(järjend)

    vastus = []
    while i <=pikkus:
        vaadeldav_järjend = []

        vaadeldav = järjend[:1+n]
    
        while len(vaadeldav) >arv:
            vaadeldav.pop(0)
        har_keskmine = harmonic_mean(vaadeldav)

        vastus.append(har_keskmine)
        n = n+1
        i = i+1
    return vastus
arv = int(input("Sisesta arv: "))
järjend = []
f = open("aktsiad.txt")
for rida in f:
     rida1 = rida.strip().split(",")
     number = rida1[-1]
     järjend.append(float(number))

järjend2 = silu_andmed(järjend, arv)

#graafik
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(järjend)
ax.plot(järjend2)
ax.set_xlabel("x")
plt.show()