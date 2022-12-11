import re

with open('aadressid.txt') as f:
    print('Kasutajanimed on:')
    for rida in f:
        otsing = re.search('http://www.ut.ee/~([a-y0-9]*)/', rida)
        if otsing:
            print(otsing.group(1))