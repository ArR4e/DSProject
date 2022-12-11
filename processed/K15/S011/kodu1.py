import re

f = open("aadressid.txt")
read = f.readlines()
f.close()

print("Kasutaja nimed on: ")
for el in read:
    kasutaja = re.search("http://www.ut.ee/~(\d+)/" , el)
    if kasutaja:
        print(kasutaja.group(1))


