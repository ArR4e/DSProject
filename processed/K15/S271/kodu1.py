import re
f = open('aadressid.txt', 'r', encoding='UTF-8')
for rida in f:
    rida = rida.strip()
    if re.match('http://www.ut.ee/~', rida):
        rida = rida.replace('http://www.ut.ee/~', '').strip()
        if re.search('/', rida):
            rida = rida.split('/')[0]
            print(rida)