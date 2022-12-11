import re
f = open('aadressid.txt', encoding = 'utf-8')
print("Kasutajanimed on: ")
for rida in f:
    koht = re.search('http://www[.]ut[.]ee/~(\w+)', rida)
    if koht:
        print(koht.group(1))
