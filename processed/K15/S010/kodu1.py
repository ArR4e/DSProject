import re

f=open('aadressid.txt', encoding='utf-8')
print('Kasutajanimed on: ')
for rida in f:
    korrastatud=rida.strip()
    if re.search('http://www.ut.ee/~(\w+)/',korrastatud):
        nimi=re.search('/~(\w+)/', korrastatud)
        print(nimi.group(1))
f.close()
