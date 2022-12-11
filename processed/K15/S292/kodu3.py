nimi = input("Sisesta faili nimi: ")

f = open(nimi)

ajad = []

for rida in f:
    rida = rida.split()
    ajad.append(rida)
    
f.close()

korras = []

for i in range(len(ajad)):
    start = str(ajad[i][0])
    l6pp = str(ajad[i][1])
    hind = int(ajad[i][2])
    sobib = 1

    for k in range(len(ajad)):
        if k != i:
            if str(ajad[k][0]) > start:
                if str(ajad[k][1]) < l6pp:
                    if int(ajad[k][2]) < hind:
                        sobib = 0
    if sobib == 1:
        korras.append(ajad[i])
        
korras.sort()
for rida in korras:
    print(*rida)