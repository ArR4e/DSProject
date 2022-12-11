import re

leiud = []
with open('aadressid.txt', encoding='utf-8') as fail:
    for rida in fail:
        try:
            leid = re.search('http://www.ut.ee/~([a-z0-9]+)', rida)
            leiud.append(leid.group(1))
        except:
            continue

print('Kasutajanimed on:')
for leid in leiud:
    print(leid)
