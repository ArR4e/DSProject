import re
def kasutajanimed(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    for line in fail.readlines():
        puhas = line.strip()
        nimi = re.search("http://www.ut.ee/~(\w+)/", puhas)
        if nimi != None:
            print(nimi.group(1))
        else:
            continue
    return nimi

print("Kasutajanimi on: ")
print(kasutajanimed("aadressid.txt"))
#ma ei tea kuidas seda None-i saada kõige lõpust ära