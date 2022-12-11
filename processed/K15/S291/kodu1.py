import re

fail = open("aadressid.txt", encoding = "UTF-8")

print("Kasutajanimed on:")

for rida in fail:
    rida = rida.strip()
    kasutajanimi = re.search("www.ut.ee/~([a-zõäöü0123456789]*?)/", rida)
    if kasutajanimi != None:
        print(kasutajanimi.group(1))