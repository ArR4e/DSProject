# regex

import re


kasutajanimed = []
with open("aadressid.txt", encoding='utf-8') as f:
    for rida in f:
        n = re.search('http?://www\.ut\.ee', rida)
        m = re.search('/~(.+?)/', rida)
        if n and m:
            kasutajanimed.append(rida[m.start()+2:m.end()-1])


print('Kasutajanimed on:')
for nimi in kasutajanimed:
    print(nimi)