from statistics import harmonic_mean
a = [11,2,3]

def silu_andmed():
    järjend = []
    uus_järjend = []
    fail = open("test.txt")   
    for rida in fail:
        if rida == "":
            break
        else:
            a = rida.strip().split(",")
            number = a[-1]
            järjend = järjend + [number]
    uus_järjend = harmonic_mean(a)
    return uus_järjend
    
    fail.close()

import matplotlib.pyplot as plt

järg = [silu_andmed()]
aeg = [0, 200, 400, 600, 800, 1000]

fig = plt.figure()          
ax = fig.add_subplot(1,1,1)  

ax.plot(järg, aeg)  
ax.set_xlabel("Graafik")       

plt.show()                   