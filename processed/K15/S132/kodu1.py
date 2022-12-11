import re

f = open('addressid.txt')

print('kasutajanimed on: ')
for rida in f:
    if re.search('ut.ee', rida.strip()):
        if re.search('/~(\w+)/', rida.strip()):
            nimi = re.search('/~(\w+)/', rida.strip())
            print(nimi.group(1))
    
    
f.close()
    