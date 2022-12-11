import re
print('kasutajanimed on:')
with open ('aadressid.txt') as file:
    for rida in file:
        if 'ut.ee/~' in rida:
            kasutaja=re.search('~(\w+)\S',rida)
            print(kasutaja.group(1))