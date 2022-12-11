import re

print('Kasutajanimed on: ')

f = open("aadressid.txt", 'r')
for rida in f:
    jarik = rida.split('/')
    nimi = r'^~\w+$'
    if  'www.ut.ee' in jarik:
        for el in jarik:
            if re.match(nimi,el):
                mustr = r'\~'
                el = re.sub(mustr,'',el)
                print(el)
f.close()   