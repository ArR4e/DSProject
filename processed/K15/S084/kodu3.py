def järjesta(lst):
    while True:
        vahetus = False
        for i in range(len(lst)-1):
            if lst[i][0] > lst[i+1][0]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                vahetus = True
        if not vahetus:
            break
fail = input("Sisesta failinimi: ")
ajad = []
with open(fail) as f:
    for line in f.readlines():
        sone = line.strip()
        line = line.replace(":","").strip().split(" ")
        ajad.append((int(line[0]),int(line[1]),int(line[2]),sone))
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
järjesta(ajad)
tulemus = []
tulemus2 = []
for i in range(len(ajad)-1):
    if ajad[i][1] < ajad[i+1][1] or ajad[i][2] < ajad[i+1][2]:
        tulemus.append(ajad[i])
tulemus.append(ajad[len(ajad)-1])
for i in range(len(tulemus)-1):
    if tulemus[i][1] < tulemus[i+1][1] or tulemus[i][2] < tulemus[i+1][2]:
        tulemus2.append(tulemus[i])
tulemus2.append(tulemus[len(tulemus)-1])
for i in tulemus2:
    print(i[3])
