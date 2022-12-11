import time
from datetime import datetime

fail = input('Sisesta failinimi: ')

algus = []
uusalgus = []
lopp = []
hind = []
sobivad = []

with open(fail, encoding = 'UTF - 8') as f:
    for rida in f:
        andmed = rida.strip().split()
        algus.append(andmed[0])
        lopp.append(andmed[1])
        hind.append(andmed[2])
        
for i in range(len(algus)):
    sobib = True
    for j in range(1, len(algus)):
        if (algus[i] < algus[j] and lopp[i] > lopp[j]) and float(hind[i]) > float(hind[j]):
            sobib = False
    if sobib:
        uusalgus.append(algus[i])
        sobivad.append(f'{algus[i]} {lopp[i]} {hind[i]}')

for i in range(len(uusalgus)):
    miinimum = min(uusalgus)
    index = uusalgus.index(miinimum)
    print(sobivad[index])
    uusalgus.pop(index)
    sobivad.pop(index)
    
