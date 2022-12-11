import datetime as t


def ajavahe(ajad):
    global i
    tund, minut = ajad[0].split(':')
    lõpp = t.timedelta(hours = int(tund), minutes = int(minut))
    tund1, minut1 = ajad[1].split(':')
    algus = t.timedelta(hours = int(tund1), minutes = int(minut1))
    vahe = (((algus - lõpp).total_seconds()) / 60) / 60
    return i, vahe, ajad[2]
                    
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min_indeks = i
        for j in range(i + 1, len(järjend)):
            if järjend[min_indeks][1] > järjend[j][1]:
                min_indeks = j
        järjend[i], järjend[min_indeks] = järjend[min_indeks], järjend[i]
    return järjend

def mull(järjend):
    n = len(järjend)
    for i in range(n):
        for j in range(0, n-i-1):
            if järjend[j][2] > järjend[j+1][2] and järjend[j][2] >= järjend[j+1][2]:
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
    return järjend

fn = input('Sisesta failinimi: ')
with open(fn, encoding = 'utf-8') as f:
    sisu = []
    i = 0
    bussid = []
    while True:
        g = f.readline()
        if g == '':
            f.close()
            break
        sisu.append((ajavahe(g.strip().split(' '))))
        bussid.append(g.strip())
        i += 1
    f.close()
    
järjekord = järjesta_punktid(sisu)  
kiireim = järjekord[0][1]
sobivad = []
for buss in sisu:
    if buss[1] <= kiireim:
        kiireim = buss[1]
        sobivad.append(buss)

print('Võiksid kaaluda järgnevaid busse: ' )
for aeg in sobivad:
    print(bussid[aeg[0]])
    
    
