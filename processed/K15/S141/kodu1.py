import re

fail = open('aadressid.txt', 'r')
read = fail.readlines()
fail.close()
print('Kasutajanimed on:')
for rida in read:
    if re.search('http://www.ut.ee/~', rida):
        nimi = rida.split('/')
        print(nimi[3].replace('~', ''))