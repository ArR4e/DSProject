f_n = str(input("Sisesta sõiduplaanide faili nimi: "))

def number(kell):
    kell = kell.split(":")
    return int(kell[0]), int(kell[1])

def printer(rida):
    for el in rida:
        print(el, end = " ")
    print()

uus_j = []
with open(f_n, "r", encoding="UTF-8") as f:
    jär = []
    for rida in f:
        rida = rida.strip().split(" ")
        jär.append(rida)

n = len(jär)

for i in range(n):
    vältund_1, välmin_1 = number(jär[i][0])
    saabtund_1, saabmin_1 = number(jär[i][1])
    hind_1 = int(jär[i][2])
    for j in range(n):
        vältund_2, välmin_2 = number(jär[j][0])
        saabtund_2, saabmin_2 = number(jär[j][1])
        hind_2 = int(jär[j][2])
        if vältund_1 < vältund_2:
            if saabtund_1 > saabtund_2:
                if hind_1 > hind_2:
                    uus_j.append(jär[i])
                    break
            elif saabtund_1 == saabtund_2:
                if saabmin_1 > saabmin_2:
                    if hind_1 > hind_2:
                        uus_j.append(jär[i])
                        break
        elif vältund_1 == vältund_2:
            if välmin_1 < välmin_2:
                if saabtund_1 > saabtund_2:
                    if hind_1 > hind_2:
                        uus_j.append(jär[i])
                        break
                elif saabtund_1 == saabtund_2:
                    if saabmin_1 > saabmin_2:
                        if hind_1 > hind_2:
                            uus_j.append(jär[i])
                            break

for el in uus_j:
    jär.remove(el)

n = len(jär)

for i in range(n-1):
        for j in range(n-i-1):
            tund_1, min_1 = number(jär[j][0])
            tund_2, min_2 = number(jär[j+1][0])
            if tund_1 > tund_2:
                jär[j], jär[j+1] = jär[j+1], jär[j]
            elif tund_1 == tund_2:
                if min_1 > min_2:
                    jär[j], jär[j+1] = jär[j+1], jär[j]
    
print("Esimesest linnast teise sõitmiseks võid kaaluda järgmisi busse:")
for el in jär:
    printer(el)