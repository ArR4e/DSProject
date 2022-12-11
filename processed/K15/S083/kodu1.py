import re

f = open('aadressid.txt', encoding='utf-8')
print('Kasutajanimed on:')
for rida in f:
    if re.match('.*[.]ee[/][~]', rida):
        nimi = re.search(r'(?<=~)\w+', rida)
        if nimi != None:
            print(nimi.group(0))

f.close()
