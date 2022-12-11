import re

nimed = []

with open("aadressid.txt", "r", encoding="UTF-8") as f:
    for rida in f:
        rida = rida.strip()
        if re.match("http://www.ut.ee/~", rida):
            nimi = rida.split("~")[1]
            if re.search("/", nimi):
                nimi = nimi.split("/")[0]
            nimed.append(nimi)
            
print("Kasutajanimed on:", *nimed, sep="\n")