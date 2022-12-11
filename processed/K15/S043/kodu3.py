from datetime import datetime
with open(str(input("Sisesta failinimi: "))) as f:
    read = f.read().splitlines()
f.close()
uus = []
for el in read:
    el = el.split(' ', 2)
    uus.append(el)
for i in range(len(uus)):
    for j in range(i, len(uus)):
        essa_aeg = datetime.strptime(uus[i][1], '%H:%M') - datetime.strptime(uus[i][0], '%H:%M')
        teine_aeg = datetime.strptime(uus[j][1], '%H:%M') - datetime.strptime(uus[j][0], '%H:%M')
        if  essa_aeg > teine_aeg:
            uus[i], uus[j] = uus[j], uus[i]

väikseim_aeg = datetime.strptime(uus[0][1], '%H:%M') - datetime.strptime(uus[0][0], '%H:%M')
perf_ajad = []
for el in uus:
    if datetime.strptime(el[1], '%H:%M') - datetime.strptime(el[0], '%H:%M') == väikseim_aeg:
        perf_ajad.append(el)
piletihinnad = []
for aeg in perf_ajad:
    piletihinnad.append(aeg[2])
miinimum_p = min(piletihinnad)
for el in uus:
    if datetime.strptime(el[1], '%H:%M') - datetime.strptime(el[0], '%H:%M') > väikseim_aeg and int(el[2]) < int(miinimum_p):
        perf_ajad.append(el)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for aeg in perf_ajad:
    print(f"{aeg[0]} {aeg[1]} {aeg[2]}")