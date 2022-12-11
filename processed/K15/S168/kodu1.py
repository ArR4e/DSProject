import re

f = open("aadressid.txt", encoding = 'utf-8')

names = []
for row in f:
    row = row.strip()
    leidub = re.match("(http://www.ut.ee/~).*", row)
    if leidub:
        osa = row.split('/~')[1]
        name = osa.split('/')[0]
        names.append(name)

print("Kasutajanimed on:")

for nimi in names:
    print(nimi)

f.close()