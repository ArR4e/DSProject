import matplotlib.pyplot as plt
from statistics import harmonic_mean
#sisendid ja failist lugemine
avatav_fail = input("sisesta andmete faili nimi: ")
n = int(input("sisesta n: "))
f = open(avatav_fail, "rt", encoding = "UTF-8")
fail = f.readlines()
f.close()

#funktsioon
def silu_andmed(fail,n):
    arvud = []
    for el in fail:
        el = el.strip().split(", ")
        arvud += [float(el[1])]
    index = n-1
    puhtad_andmed = []
    s = 1
    for i in range(len(arvud)):
        if i <= index:
            puhtad_andmed += [harmonic_mean(arvud[0:i+1])]
        elif i > index:
            puhtad_andmed += [harmonic_mean(arvud[s:i+1])]
            s += 1
    return puhtad_andmed


#siltide list
sildid = []
for el in fail:
    el = el.strip().split(", ")
    sildid += [el[0]]


#graafiku kuvamine
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(sildid, silu_andmed(fail,n))
ax.set_xlabel("kuupäev")
plt.show()


        
