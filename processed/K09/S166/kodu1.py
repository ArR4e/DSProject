from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend,arv):
    silutud_andmed=[]
    jagaja=0
    if len(järjend)==0:
        return silutud_andmed
    for i in range(arv):
        if i>=len(järjend):
            break
        jagaja+=(1/järjend[i])
        silutud_andmed+=[(i+1)/(jagaja)]
    if arv>len(järjend):
        return silutud_andmed
    for i in range(len(järjend)-arv):
        silutud_andmed+=[harmonic_mean(järjend[i+1:arv+i+1])]
    return silutud_andmed
failinimi= input("Sisesta failinimi: ")
fail = open(failinimi,'r')
järjend = []
kuupäevad = []
for rida in fail:
    rida = rida.strip().split(',')
    järjend+=[float(rida[1])]
    kuupäevad+=[rida[0]]
print(len(järjend))
silutud_andmed=silu_andmed(järjend,50)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(kuupäevad, järjend, "-", label="aktsia hind")
ax.plot(kuupäevad, silutud_andmed, "-", label="keskmine aktsia hind")
ax.set_xlabel("kuupäevad")
ax.set_ylabel("hinnad")
ax.set_ylim(0,0.02)
ax.set_xticks([0,200,400,600,800,1000])
ax.legend()
plt.show()