from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(a, n):
    andmed = []
    for i in range(len(a)):
        if i < n:
            andmed.append(harmonic_mean(a[:i+1]))
        else:
            andmed.append(harmonic_mean(a[i-(n-1):i+1]))
    return andmed

fail = input('Sisesta faili nimi: ')

with open(fail) as f:
    päevad = 0
    hinnad = ''
    for i in f:
        päevad += 1
        hinnad += i[13:]
    hinnad = hinnad.split('\n')
    hinnad = [float(x) for x in hinnad]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(range(päevad), hinnad, label='Silutud andmed')
ax.plot(range(päevad), silu_andmed(hinnad, 50), label='Algandmed')
ax.set_xlabel('Päev')
ax.set_ylabel('Hind')

plt.show()