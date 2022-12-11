f = open(input("Sisesta failinimi: "))
jär = []
for rida in f:
    jär.append(rida.strip())

for i in range(len(jär)):
    for j in range(i+1, len(jär)):
        if int(jär[j].split(":")[0]) < int(jär[i].split(":")[0]):
            jär[i], jär[j] = jär[j], jär[i]
            if int(jär[j].split(":")[0]) < int(jär[i].split(":")[0]):
                jär[i], jär[j] = jär[j], jär[i]
                if int(jär[j].split(":")[1].split(" ")[0]) < int(jär[i].split(":")[1].split(" ")[0]):
                    jär[i], jär[j] = jär[j], jär[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for i1 in range(len(jär)):
    for j1 in range(i1+1, len(jär)):
        if jär[j1].split(" ")[0] >= jär[i1].split(" ")[0] and jär[j1].split(" ")[1] <= jär[i1].split(" ")[1] and jär[j1].split(" ")[2] <= jär[i1].split(" ")[2]:
            print(jär[j1])