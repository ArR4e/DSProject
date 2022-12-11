import re

fail = open("aadressid.txt", encoding="utf-8")
leidub = 0

for rida in fail:
    kasutaja = r"http://www.ut.ee/~\S+/"
    kasutaja2 = r"http://www.ut.ee/~"
    var1 = re.search(kasutaja, rida)
    if var1:
        if leidub == 0:
            leidub += 1
            print("Kasutajanimed on: ")
            eralda = re.sub(kasutaja2,"", rida)
            eralda = eralda.replace('/',' ')
            lahku = eralda.split()
            kasutaja_nimi = lahku[0]
            print(kasutaja_nimi)
        elif leidub == 1:
            eralda = re.sub(kasutaja2,"", rida)
            eralda = eralda.replace('/',' ')
            lahku = eralda.split()
            kasutaja_nimi = lahku[0]
            print(kasutaja_nimi)
fail.close()