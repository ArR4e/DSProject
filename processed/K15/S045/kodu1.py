import re
with open('aadressid.txt', 'r', encoding='UTF-8') as f: data = f.read()
print('Kasutajanimed on:')
for nimi in re.findall("ut\.ee\/~([^\s][^/]*)", data): print(nimi) #kasutasin https://regexr.com/ regulaaravaldise tegemiseks