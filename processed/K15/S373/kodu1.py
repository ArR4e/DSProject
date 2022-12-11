import re
fail = open("aadressid.txt", "r", encoding="UTF-8")
print("Kasutajanimed on:")
for rida in fail:
    for kasutajanimi in re.finditer("http://www.ut.ee/~(?:[a-z]|[0-9])+/", rida):
        andmed = kasutajanimi.group().split("~")
        print(andmed[-1].strip("/"))