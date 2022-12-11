import re

print("Kasutajanimed on:")
f = open("aadressid.txt", "r", encoding="utf-8")
for rida in f:
    leiud = re.search('http://www.ut.ee/~([a-z, 0-9]+)', rida)
    if leiud:
        on = leiud.groups(1)
        sõne = ''.join(on)
        print (sõne)