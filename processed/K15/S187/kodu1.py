import re

f = open('aadressid.txt', 'r')

print('Kasutajanimed on:')
for rida in f.readlines():
    if re.search('http://www.ut.ee/~', rida):
        print(re.search('~(.*)/', rida).group(1))
f.close()