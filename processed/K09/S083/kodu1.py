from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(algandmed, n):
    m=0
    silutud = []
    while m < len(algandmed):
        if m < n:
            silutud += [harmonic_mean(algandmed[:m+1])]
            m+=1
            continue
        else:
            järjend = list(algandmed[(m-(n-1)):m+1])
            silutud.append(harmonic_mean(järjend))
            m+=1
            continue
    return silutud

f = input('Sisesta faili nimi: ')
n = int(input('Sisesta positiivne täisarv: '))
fail = open(f)
read = fail.readlines()
väärtused = [i.split(',')[1].strip() for i in read]
arvud = []
for sõne in väärtused:
    arvud = arvud + [float(sõne)]

fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
ax.plot(arvud, label='aktsia hinnad')
ax.plot(silu_andmed(arvud, n), label = 'silutud andmed')
ax.set_xlim(0, len(arvud))
ax.set_xlabel('Päevad')
ax.legend()
plt.show()
    
    