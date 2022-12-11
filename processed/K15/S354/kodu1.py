import re
# if http://www.ut.ee/~
print('Kasutajanimed on:')
f = open('aadressid.txt')

for rida in f:
    rida = rida.strip()
    if re.search('http://www.ut.ee/~', rida):
        rida = rida.split('http://www.ut.ee/~')
        for el in rida:
            el = el.split('/')
            if el != '':
                print(el[0])



    