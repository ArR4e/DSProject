# Regulaaravaldis
import re

fail = open('aadressid.txt', 'r')

print('Kasutajanimed on:')

for rida in fail:
    if  re.search('http://www.ut.ee/~', rida):
        kasutajanimi = re.findall(r'~(\w+)', rida)
        if kasutajanimi != []:
            print(kasutajanimi[0])

fail.close()