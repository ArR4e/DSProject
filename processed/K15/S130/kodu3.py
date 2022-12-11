#Bussid + pole lõpetatud

fail = input('Sisesta s6iduplaanidega faili nimi: ')
print('Esimesest linnast teise s6itmiseks v6iksid kaaluda neid busse:')


f = open(fail, 'r')
plaan = {}
ajad = f.readlines()
plaan = []
for el in ajad:
    plaan.append(el.strip().split(' '))
sobivad = []    
for i in range(len(plaan)):
    for j in range(0, len(plaan)):
        if plaan[i][0] <= plaan[j][0]:
            if plaan[i][1] <= plaan[j][1]:
                if plaan[i][2] <= plaan[j][2]:
                    if plaan[i] not in sobivad:
                           print(plaan[i])
                    
