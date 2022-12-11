import re

f = open("aadressid.txt", encoding="UTF-8")
print("Kasutajanimed on:")

for el in f:
    if re.search("www.ut.ee/~", el):
        if re.search("/(~)[a-z]", el):
            el = el.split("~")[1].lstrip().split("/")[0]
            print(el)
            
f.close()