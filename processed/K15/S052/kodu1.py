f = open("aadressid.txt", encoding="UTF-8")

print("Kasutajanimed on:")

for i in f:
    if "/" in i and "www.ut.ee" in i:
        parts = list(i.split("/"))
        for e in parts:
            if "~" in e:
                print(e[1::])
                break
            else:
                continue
    else:
        continue
