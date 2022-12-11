import re

with open('aadressid.txt') as f:
    tekst = f.readlines()

print('kasutajanimed on:')

for rida in tekst:
    tulemus = re.search('http://www.ut.ee/~[^ ]*?/', rida)
    if tulemus != None:
        print(tulemus.group()[18:-1])