# 1. Regulaaravaldis

import re

fail = "aadressid.txt"

print("Kasutajanimed on:")
f = open(fail, "r", encoding="UTF-8")
for rida in f:
    a = rida.strip()
    if re.search("www.ut.ee", a) and re.search("http:", a):
        vastus = re.findall(r'http://www.ut.ee/~(\w+)/', a)
        if vastus != []:
            vastus = vastus[0]
            print(vastus)

