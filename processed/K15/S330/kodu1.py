import re

f = open("aadressid.txt", encoding = "UTF-8")
kasutajanimed = []
for rida in f:
    if re.search("www.ut.ee/~(\w+)/", rida) != None:
        kasutajanimi = re.search("www.ut.ee/~(\w+)/", rida)
        kasutajanimed.append(kasutajanimi.group(1))
f.close()

print("Kasutajanimed on: ")
for nimi in kasutajanimed:
    print(nimi)