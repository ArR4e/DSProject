import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(list, n):
    if n > len(list):
        n = len(list)
    try:
        list_of_means = []
        for i in range(n - 1):
                mean = harmonic_mean(list[:(i + 1)])
                list_of_means.append(mean)
        while True:
            if len(list) < n:
                break
            mean = float(harmonic_mean(list[:n]))
            list.pop(0)
            list_of_means.append(mean)
    except:
        pass
    return list_of_means

fail = input("Sisesta faili nimi: ")
f = open(fail)
hindade_list = []
days = []
count = 1
for rida in f:
    rida = rida.split(',')
    days.append(count)
    hindade_list.append(float(rida[1].strip()))
    count += 1
f.close()
n = int(input("Sisesta n: "))


list = hindade_list[:]
list_of_means = silu_andmed(hindade_list, int(n))


plt.plot(days, list_of_means)
plt.plot(days, list)
plt.show()

    
            