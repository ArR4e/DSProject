from datetime import datetime, timedelta
import re

fail = input('Sisesta failinimi: ')
f = open(fail, 'r')

bussid = f.readlines()

koik = {}
lyhim = 99999999
for rida in bussid:
    rida = rida.split(' ')
    algus = float(rida[0][:2]) + float(rida[0][3:])/60
    lopp = float(rida[1][:2]) + float(rida[1][3:])/60
    aeg = lopp - algus
    koik[aeg] = rida[2]
    if aeg < lyhim:
        lyhim = aeg

sobivad = []
sobivad_hinnad = []
sobivad_algused = []
sobivad_dict = {}
for rida in bussid:
    rida1 = rida.split(' ')
    algus = float(rida1[0][:2]) + float(rida1[0][3:])/60
    lopp = float(rida1[1][:2]) + float(rida1[1][3:])/60
    aeg = lopp - algus
    if aeg == lyhim:
        sobivad.append(rida.strip())
        sobivad_hinnad.append(rida1[2])
        sobivad_algused.append(algus)
        sobivad_dict[algus] = rida.strip()

for buss in koik:
    if koik[buss] < min(sobivad_hinnad):
        sobivad.append(buss)
        algus = float(koik[buss][0][:2]) + float(koik[buss][0][3:])/60
        sobivad_algused.append(algus)
        sobivad_dict[algus] = koik[buss]

for i in range(len(sobivad_algused) - 1):
    for j in range(len(sobivad_algused) - i - 1):
        if sobivad_algused[j] > sobivad_algused[j + 1]:
            sobivad_algused[j], sobivad_algused[j + 1] = sobivad_algused[j + 1], sobivad_algused[j]

print('Võiksid kaaluda neid busse:')
for aeg in sobivad_algused:
    print(sobivad_dict.pop(aeg))