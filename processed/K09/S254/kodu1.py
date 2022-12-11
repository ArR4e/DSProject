from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(jär,n):
    algandmed=[]
    andmed=[]
    silutud=[]
    for rida in jär:
        hind = float(rida)
        andmed.append(hind)
        algandmed.append(hind)
        if len(andmed) > n:
            andmed.pop(0)
            elem1=harmonic_mean(andmed[:])
            silutud.append(elem1)
        else:
            elem=harmonic_mean(andmed[:])
            silutud.append(elem)
    return silutud

fail=open('aktsiad.txt',encoding='UTF-8')
read=fail.readlines()
fail.close()
faili_jär=[]
for rida in read:
    hind = float(rida.split(', ')[1].strip())
    faili_jär.append(hind)

silutud = silu_andmed(faili_jär,50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(faili_jär)
ax.plot(silutud)
plt.show()
