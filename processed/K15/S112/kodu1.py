import re

f = open('aadressid.txt','r',encoding = 'UTF-8')

for rida in f:
    if re.search('ut\.ee/\~',rida.strip()):
        nimi = re.search('ut\.ee/\~(\w+)/', rida)
        try:
            print(nimi.group(1))
        except:
            continue
        
f.close()