import re

f = open('aadressid.txt', encoding='utf-8')

print('Kasutajanimed on:')

for rida in f:
    if re.search(r'http://www\.ut\.ee/~[a-z0-9]', rida):
        a = re.search('~([a-z0-9]*)/', rida)
        print(a.group(1))

f.close()