fail = input('Sisesta faili nimi: ')
f = open(fail)

read = []
ajad = []
eivali = []
for rida in f: #teeb iga rea omaette listiks
    rida = rida.strip('\n').split(' ')
    ajad.append(rida)

for i in range(len(ajad)): #kontrollib kõik ajad üksteisega ja leiab millised sobivad, millised mitte
    for j in range(len(ajad)):
        if ajad[i][0] > ajad[j][0] and ajad[i][1] < ajad[j][1] and float(ajad[i][2]) < float(ajad[j][2]):
            eivali.append(ajad[j])

for i in range(len(ajad)):
    for j in range(i, len(ajad)):
        if ajad[i][0] > ajad[j][0]:
            ajad[j], ajad[i] = ajad[i], ajad[j]

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for i in ajad:
    lause = ''
    if i not in eivali:
        for j in i:
            lause += j+' '
        print(lause)