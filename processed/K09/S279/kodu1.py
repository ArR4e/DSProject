faili_nimi = input("Sisesta faili nimi: ")
fail = open(faili_nimi, encoding="UTF-8")

sõnede_järjend = []
for rida in fail:
    rida = rida.strip().split(", ")
    sõnede_järjend.append(rida[1])
järjend = [float(arv) for arv in sõnede_järjend]

fail.close()

from statistics import harmonic_mean

def silu_andmed(järjend, arv):
    väiksem_järjend = järjend[(n+1)-arv:n+1]
    for element in järjend:
        
        hind = järjend.pop(0)
        keskmine = harmonic_mean(väiksem_järjend)
        järjend.append(keskmine)
        
# järjend = [2, 1, 3, 4, 5]
# 
# silu_andmed(järjend, 3)