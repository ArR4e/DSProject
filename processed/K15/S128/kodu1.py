import re

fail = open("aadressid.txt", encoding = "utf-8")
aadressid = []
for rida in fail:
    aadressid.append(rida.strip())

print("Kasutajanimed on: ")
for rida in aadressid:
    if re.match("http://www.ut.ee/~", rida):
        kasutaja = rida[rida.index("~")+1:rida.index("/",17)]
        print(kasutaja)
