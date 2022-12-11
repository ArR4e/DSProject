from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(lst,taisarv):
    #harmoonilise keskmisega
    end_lst =[]
    for i in range(len(lst)):
        if i< taisarv:
            end_lst += [harmonic_mean(lst[:i+1])]
        else:
            end_lst += [harmonic_mean(lst[i-taisarv:i])]  
#    end_lst += [harmonic_mean(lst[len(lst)-taisarv:])] 
    return end_lst

#print(silu_andmed([2, 1, 3, 4, 5], 3))

kuud = []
saktsiad = []
f = open("aktsiad.txt","r")
for rida in f:
    a = rida.strip("\n").split(", ")
    aktsiad += [float(a[1])]
    kuud += [a[0]]
f.close()



sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]

fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(kuud, aktsiad)  # Lisame joonestusalale joondiagrammi

ax.set_xticks([0,200,400,600,800,1000])

plt.show()    