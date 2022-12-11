fail = input("Sisesta failinimi: ")
f = open(fail)

ajad = []
hinnad = []
info = {}

def järjesta_punktid(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):                       
            if arr[j][0] > arr[j + 1][0] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for rida in f:
    k = rida.strip()
    rida = rida.strip().split(" ")
    alguse_aeg = rida[0].split(":")
    algus = int(alguse_aeg[0]) + float(alguse_aeg[1])/60
    lõpu_aeg = rida[1].split(":")
    lõpp = int(lõpu_aeg[0]) + float(lõpu_aeg[1])/60
    hind = int(rida[2])
    ajad.append((algus, lõpp, hind, k))
       
järjesta_punktid(ajad)
ei_sobi = []

for i in range(len(ajad) - 1):
    for j in range(i+1, len(ajad)):
        if ajad[i][1] > ajad[j][1] and ajad[i][2] > ajad[j][2]:
            ei_sobi.append(ajad[i])

print("Sõitmiseks võiks kaaluda järgmisi busse:")

for i in ajad:
    if i not in ei_sobi:
        print(i[3])