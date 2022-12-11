from statistics import harmonic_mean
fail = open('aktsiad.txt')
d = 1
k = [5,6,7,8,9]
n = 10
hinnad = []
q = 1
def silu_andmed(hinnad,täisarv):
    uus = []
    d = 1
    b = 1
    while True:
        #while täisarv != d:
            #if hinnad == []:
                #break
        while True:
            #k = hinnad.pop.(0)
            if hinnad == []:
                break
            elif d == 1:
                arv = harmonic_mean([hinnad[0]])
                d = d + 1
                b = b + 1
                uus.append(arv)
                k = hinnad.pop(0) 
            elif d>1 and b == 2 :
                arv = harmonic_mean([k]+hinnad[0:(b-1)])
                if arv != uus[-1]:
                    uus.append(arv)
                
                b = b +1
                d = d + 1
                    #täisarv = täisarv + 1

            elif d > 2 and täisarv > (b-1) :
                b = b-1
                arv = harmonic_mean([k]+hinnad[0:b])
                if arv != uus[-1]:
                    uus.append(arv)
                else:
                    break
                b = b + 2

            elif len(hinnad) >= täisarv: #len(hinnad)> täisarv and len(hinnad)>d:
                arv = harmonic_mean(hinnad[0:täisarv])
                uus.append(arv)
                k = hinnad.pop(0)
            else:
                break

                
        return(uus)

while True:
    a = fail.readline()
    if a == '':
        break
    e = a.split()
    hinnad.append(float(e[-1]))

vanad = hinnad[:]
uued =print(silu_andmed(hinnad,n))
fail.close()

import matplotlib.pyplot as plt
import numpy as np

kuud = [0,1025]
uusim = uued
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ypoints = np.array(vanad)
ypoints2 = np.array(uusim)
plt.plot(ypoints)
plt.plot(ypoints2)
#ax.plot(kuud,vanad)
#ax.plot(kuud,uusim)
ax.set_xlabel("Kuud")

plt.show()