from statistics import harmonic_mean
import matplotlib.pyplot as plt
import copy

def silu_andmed(järjend, n):
    if järjend != []:
        keskmised = []
        viimased = järjend[(len(järjend)-n):]
        for i in range(1,len(järjend)):
           järjend.pop(-1)
           n_elementi = järjend[-n:] 
           keskmised.append(harmonic_mean(n_elementi))
        oigekeskmised = keskmised[::-1]
        oigekeskmised.append(harmonic_mean(viimased))   
        return oigekeskmised
    else:
        return []      

#loe failits andmed 
f = open('aktsiad.txt')
päev = []
hind = []
i = 0
for rida in f:
    rea_osad = rida.strip("\n").split(",")
    hind.append(float(rea_osad[-1].strip(' ')))
    päev.append(int(i))
    i += 1
f.close()


#arvutame keskmise
hinnad = copy.deepcopy(hind)
keskmine = silu_andmed(hind, 50)

#joonis
fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

ax.plot(päev, hinnad, label = "hinnad") 
ax.plot(päev, keskmine, label = "silutud hinnad")
ax.set_xlabel("Päev")     

ax.set_ylim(0, 0.02)        
ax.set_xticks([0,200,400,800,1000]) 

plt.show()              

