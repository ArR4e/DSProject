import re

f = open("aadressid.txt", encoding="utf-8")
text = f.readlines()
f.close()

print("Kasutajanimed on:")
for rida in text:
    if re.search("www.ut.ee/~", rida):
        ridA = rida.strip().split("/")
        nimi = ridA[3].strip("~")
        print(nimi)
    