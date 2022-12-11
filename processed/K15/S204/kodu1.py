import re

f = open("aadressid.txt",encoding="UTF-8")

l = r"ut[.]ee/~(\w+)"

print("Kasutajanimed on: ")

for rida in f:
    v=re.search(l, rida)
    if v != None:
        uusv = v.group()
        sp = uusv.split("~")
        print(sp[1])