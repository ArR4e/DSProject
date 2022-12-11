# Ei saa aru miks automaatkontroll tahab osasi väljundeid. Programmi pakutud kellajad ja hinnad tunduvad paremad.
# Näiteks: Oodatav väljund oli: 11:00 13:00 5  ja 12:00 14:00 6
# Aga programm väljastab 11:00 13:00 5 - mis on ju odavam. 


def järjesta(välja,kohal,hind): # kasutasin kodu2 ülesande lahendust,et kellaajad järjestada
    väärtus = False
    for i in range(1,len(välja),1):
        if välja[i-1] > välja[i]:
            välja[i-1],välja[i] = välja[i],välja[i-1]
            kohal[i-1],kohal[i] = kohal[i],kohal[i-1]
            hind[i-1],hind[i] = hind[i],hind[i-1]
            väärtus = True
    
    if väärtus == True:
        return järjesta(välja,kohal,hind)
    else:
        return [välja ,kohal, hind]
    
def sorteeri(järjend):
    väärtus = False
    if len(järjend[0]) > 1:
        algus = []
        lõpp = []
        hind = []
        for i in range(1,len(järjend[0]),1):
            if järjend[0][i-1] < järjend[0][i] and järjend[1][i-1] > järjend[1][i] and int(järjend[2][i-1]) > int(järjend[2][i]):
                if järjend[0][i] not in algus:
                    algus.append(järjend[0][i])
                    lõpp.append(järjend[1][i])
                    hind.append(järjend[2][i])
                    väärtus = True
            else:
                if järjend[0][i-1] not in algus:
                    algus.append(järjend[0][i-1])
                    lõpp.append(järjend[1][i-1])
                    hind.append(järjend[2][i-1])
                
    if väärtus == True:
        uus = [algus,lõpp,hind]
        return sorteeri(uus)
    else:
        return järjend

f = input('Sisesta failinimi: ')
välja = []
kohal = []
hind = []

with open(f) as fail:
    for rida in fail:
        rida = rida.strip().split(' ')
        välja.append(rida[0])
        kohal.append(rida[1])
        hind.append(rida[2])
                
            
sorteeritud = sorteeri(järjesta(välja,kohal,hind))
pikkus = len(sorteeritud[0])
print(f'Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

for i in range(pikkus):
    print(str(sorteeritud[0][i]),str(sorteeritud[1][i]),str(sorteeritud[2][i]))