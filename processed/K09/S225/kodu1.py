from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    välja=[]
    vahejärjend=[]
    for i in range(len(järjend)):
        vahejärjend.append(järjend[i])
        if len(vahejärjend) > n:
            vahejärjend.pop(0)
        välja.append(harmonic_mean(vahejärjend))
    return välja

fail = input('Sisestage fail: ')
aktsiad_fail = open(fail, encoding = 'UTF-8')

hinnad = []
nr = 50

for rida in aktsiad_fail:
    rida = rida.replace('\n' ,'').strip(' ').split(',')
    hinnad.append(float(rida[1].strip(' ')))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hinnad, label='Silumata')
ax.plot(silu_andmed(hinnad,nr), label='Silutud')
ax.set_xticks([0, 200,400,600,800,1000])
ax.legend()
plt.show()

f.close()