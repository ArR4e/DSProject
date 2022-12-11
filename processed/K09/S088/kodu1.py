from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(a, b):
    b = abs(b)
    al = 0
    l = 1
    uuslist = []
    for i in range(len(a)):
        if l < b:
            keskmine = harmonic_mean(a[al:l])
            l += 1
            uuslist.append(keskmine)
        elif l >= b:
            keskmine = harmonic_mean(a[al:l])
            l += 1
            al += 1
            uuslist.append(keskmine)
    return uuslist

n = int(input("Sisestage täisarv, mis näitab, mitme elemendi kaupa keskmistamist rakendatakse: "))
f = open("aktsiad.txt", encoding = "UTF-8")
alg_andmed = []
p = []
a = 1
for i in f:
    i = i.split(",")
    alg_andmed.append(float(i[1]))
    p.append(a)
    a += 1
f.close()

silutud_andmed = silu_andmed(alg_andmed, n)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.plot(p, alg_andmed)
plt.plot(p, silutud_andmed)

plt.show()
