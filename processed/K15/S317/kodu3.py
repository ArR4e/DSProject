failinimi = input("Sisesta failinimi: ")
fail = open(failinimi, "r", encoding="UTF-8")
järjend = []
for i in fail:
    i = i.strip().split(" ")
    järjend.append(i)
uus = []
for i in järjend:
    for j in järjend:
        if (i[0] < j[0] and i[1] > j[1]) and int(i[2]) > int(j[2]):
            if i not in uus:
                uus.append(i)
for i in uus:
    järjend.remove(i)
for i in range(3):
    for i in range(2, len(järjend)+1, 1):
        if järjend[i-2][0] > järjend[i-1][0]:
            järjend[i-2],järjend[i-1] = järjend[i-1],järjend[i-2]
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for i in järjend:
    print(i[0], i[1], i[2])
        