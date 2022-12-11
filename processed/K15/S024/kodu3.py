fail = input("Sisesta failinimi: ")

f = open(fail)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

jär = []
for rida in f:
    rida = rida.strip().split(" ")
    jär.append(rida)

uus_jär = []
for i in range(len(jär)):
    for j in range(len(jär)):
        if jär[j][0] > jär[i][0] and jär[i][1] > jär[j][1] and float(jär[i][2]) > float(jär[j][2]):
            if jär[i] not in uus_jär:
                uus_jär.append(jär[i])
for el in uus_jär:
    jär.remove(el)
    
for i in range(len(jär)):
    varaseima_indeks = i
    for j in range(i+1, len(jär)):
        if jär[j][0] < jär[i][0]:
            varaseima_indeks = j
    if i != varaseima_indeks:
        jär[i], jär[varaseima_indeks] = jär[varaseima_indeks], jär[i]

for i in range(len(jär)):
    print(" ".join(jär[i]))
    
f.close()
