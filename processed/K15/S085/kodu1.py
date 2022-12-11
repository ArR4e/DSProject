import re

fail = open("aadressid.txt", encoding="utf-8")
print('Kasutajanimed on: ')
for rida in fail:
    a = re.search("http://www.ut.ee/~([a-zA-Z0-9_.-]+)",rida)
    if a:
        leidub = a.groups(1)
        nimi = ''.join(leidub)
        print(nimi)