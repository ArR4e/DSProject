import re

f = open("aadressid.txt", encoding="UTF-8")
kasutajad = []
for rida in f:
    rida = rida.strip()
    if re.match("http://www.ut.ee/~", rida):
        rida = rida.split("/")
        for el in rida:
            if "~" in el:
                kasutajad.append(el[1:])
                

print("Kasutajanimed on:")
for el in kasutajad:
    print(el)
        