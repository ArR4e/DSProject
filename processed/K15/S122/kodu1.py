import re

f = open("aadressid.txt",encoding="UTF-8")

print("Kasutajanimed on: ")

for rida in f:
    rida=rida.strip()
    if re.search ("http://www.ut.ee/~[a-z]",rida):
        rida_list = (rida.split("/"))
        nimi= rida_list[3].replace("~","")
        print(nimi)

f.close()