fail = open(input("Sisesta faili nimi: "), "r", encoding="UTF-8")

lst = []
read = fail.readlines()

for i in read:
    i = i.strip().split(" ")
    i[0] = i[0].split(":")
    i[0] = int(i[0][0] + i[0][1])
    i[1] = i[1].split(":")
    i[1] = int(i[1][0] + i[1][1])
    i[2] = int(i[2])
    lst.append(i)
    
removelst = []

for j in range(len(lst)):
    for k in range(len(lst)):
        if int(lst[j][0]) < int(lst[k][0]) and int(lst[j][1]) > int(lst[k][1]) and lst[j][2] > lst[k][2]:
            removelst.append(lst[j])
            
for l in removelst:
    try:
        lst.remove(l)
    except:
        pass
    
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")

for u in range(len(lst)):
    for v in range(u+1, len(lst)):
        if lst[u][0]>lst[v][0]:
            lst[u],lst[v] = lst[v],lst[u]

for m in lst:
    m[0] = str(m[0])
    m[0] = m[0][:-2] + ":" + m[0][-2:]
    if len(m[0]) == 4:
        m[0] = "0" + m[0]
        
    m[1] = str(m[1])
    m[1] = m[1][:-2] + ":" + m[1][-2:]
    if len(m[1]) == 4:
        m[1] = "0" + m[1]
    
    print(m[0] + " " + m[1] + " " + str(m[2]))

fail.close()