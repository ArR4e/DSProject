import re
f = open('aadressid.txt', encoding='UTF-8')

print("Kasutajanimed on:")
for rida in f:
    sõne = re.search('www.ut.ee/~([0-z]*)/', rida)
    if sõne != None:
       print(sõne.group(1))
