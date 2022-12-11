import statistics
import matplotlib.pyplot as plt

#kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
#sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]

#plt.plot(kuud, sissetulekud)  # Lisame joonestusalale joondiagrammi
#plt.xlabel("Kuud")            # ja x-telje pealkirja

#plt.show()


def silu_andmed(loend, n):
    for i in range(len(loend)):
        kesk_loend = []
        kesk_loend.append(statistics.harmonic_mean(loend[slice(i-1, n+i)]))
    print(kesk_loend)