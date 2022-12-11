import re

f = open("aadressid.txt", encoding = "UTF-8")
print("Kasutajanimed on:")

for rida in f:
    k = re.search("http://www.ut.ee/~(\w+)/", rida)
    if k:
        print(k.group(1))
    else:
        continue
