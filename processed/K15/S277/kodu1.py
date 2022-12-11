import re

f = open('aadressid.txt', 'r', encoding = 'utf-8')
read = f.read().split('\n')

print('Kasutajanimed on:')

for rida in read:
    if re.match(' *http://w{3}.ut.ee/~.*', rida):
        print(rida.split('~')[1].split('/')[0])
f.close()