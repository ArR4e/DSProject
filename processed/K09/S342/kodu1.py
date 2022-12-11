from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(a, n): 
    järjendSamm = []
    keskJärjend = []
    for elem in a:
        järjendSamm.append(elem)    
        if len(järjendSamm) > n:
            järjendSamm.pop(0)
        silutud_elem = harmonic_mean(järjendSamm)
        keskJärjend.append(silutud_elem)
    return keskJärjend
f = open(input("Sisestage faili nimi: "))
fsisu = f.readlines()
järjend = []
for rida in fsisu:
    x = rida.split(', ')
    järjend.append(float(x[1].strip()))
silutud = silu_andmed(järjend, 50)
f.close()
x_telg = []
x_kordaja = 1
for elem in silutud:
    x_telg.append(x_kordaja)
    x_kordaja += 1
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x_telg, järjend)
ax.plot(x_telg, silutud)

plt.show()
