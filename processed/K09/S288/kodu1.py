from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    x = 0
    silutud_järjend = []
    while x < len(järjend):
        if x < n:
            silutud_järjend += [harmonic_mean(järjend[:x+1])]
            x += 1
            continue
        else:
            uus_järjend = list(järjend[(x - (n - 1)):x+1])
            silutud_järjend.append(harmonic_mean(uus_järjend))
            x += 1
            continue
    return silutud_järjend

fail = input('Sisestage failinimi: ')
n = int(input('Sisestage positiivne täisarv: '))

with open(fail, encoding = 'UTF-8') as f:
    read = f.readlines()

väärtused = [i.split(',')[1].strip() for i in read]
hinnad = []
for y in väärtused:
    hinnad = hinnad + [float(y)]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hinnad, label = 'Aktsia hinnad')
ax.plot(silu_andmed(hinnad, n), label = 'Silutud andmed')
ax.set_xlim(0, len(hinnad))
ax.set_xlabel('Päevade arv')
ax.legend()
plt.show()