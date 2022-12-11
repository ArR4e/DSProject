# bussid

sisend = input('Sisesta failinimi: ')

def get_list(fail="sõiduplaan.txt"):
    j = []
    with open(fail, encoding="utf-8") as f:
        for rida in f:
            väljumine, saabumine, hind = rida.strip().split()
            j.append([väljumine, saabumine, hind])
            
    return j

#võetud kodu2 ülesandest
def järjesta_punktid(arr):
    pikkus = len(arr)
    for i in range(pikkus):
        for j in range(0, pikkus-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            

arr = get_list(sisend)
sõiduplaan = []
indeks = 0
for el in arr:
    väljuv, saabuv, hind = el[0], el[1], el[2]

    tunnid1, minutid1 = väljuv.split(':')
    minutid_alguses = int(tunnid1)*60 + int(minutid1)
    
    tunnid2, minutid2 = saabuv.split(':')
    minutid_lõpus = int(tunnid2)*60 + int(minutid2)
    sõiduplaan.append([minutid_lõpus-minutid_alguses, int(hind), indeks])
    indeks += 1

järjesta_punktid(sõiduplaan)

suurim = sõiduplaan[0][0]
eemaldada = []
for el in sõiduplaan:
    if el[0] > suurim:
        eemaldada.append(el)

for el in eemaldada:
    sõiduplaan.remove(el)

tulemus = []
for el in sõiduplaan:
    tulemus.append(arr[el[2]])


tulemus.sort()
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for el in tulemus:
    print(f'{el[0]} {el[1]} {el[2]}')
    
    
    
