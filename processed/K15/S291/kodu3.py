sõiduplaan = input("Sisesta failinimi: ")
fail = open(sõiduplaan, encoding= "UTF-8")

järjend = []
for rida in fail:
    rida = rida.strip().split(" ")
    järjend.append(rida)

mittesobiv_järjend = []
for i in range(len(järjend)):
    for j in range(len(järjend)):
        if järjend[i][0] < järjend[j][0] and järjend[i][1] > järjend[j][1] and float(järjend[i][2]) > float(järjend[j][2]):
            if järjend[i] not in mittesobiv_järjend:
                mittesobiv_järjend.append(järjend[i])
            
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

for buss in mittesobiv_järjend:
    järjend.remove(buss)

for i in range(len(järjend)):
    for j in range(i + 1, len(järjend)):
        if järjend[i][0] > järjend[j][0]:
            järjend[i], järjend[j] = järjend[j], järjend[i]

for i in range(len(järjend)):
    print(" ".join(järjend[i]))