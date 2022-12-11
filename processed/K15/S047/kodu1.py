import re

f = open("aadressid.txt", "r")
read = f.readlines()
f.close()

for rida in read:
    kasutaja = re.search("/~(\w+)/", rida)
    if kasutaja:
        print(kasutaja.group(0))