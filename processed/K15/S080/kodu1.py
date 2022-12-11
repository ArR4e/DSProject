import re

fail = open('aadressid.txt', encoding='utf-8')
print('Kasutajanimed on:')
for rida in fail:
    if re.search('www.ut',rida):
        algus = re.search('~',rida)
        if algus:
            a = re.search('~(\w+)',rida)
            print(a.group(1))
fail.close()    
