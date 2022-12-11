import re

fail = 'aadressid.txt'

print('Kasutajanimed on:')

with open(fail, encoding = 'UTF-8') as f:
    for rida in f:
        if re.match('.*http://www.ut.ee/~',rida):
            index = rida.index('~')
            kasutajanimi = rida[index+1:]
            if not kasutajanimi.startswith(' '):
                index = kasutajanimi.index('/')
                kasutajanimi = kasutajanimi[:(index)]
                print(kasutajanimi)

