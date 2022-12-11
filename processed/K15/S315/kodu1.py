import re

with open ('aadressid.txt', 'r', encoding = 'utf-8') as f:
    for rida in f:
        if re.match('^http://www.ut.ee/~', rida.strip()):
            nimeleht = rida.split('~')
            nimi = nimeleht[1].split('/')
            print(nimi[0])