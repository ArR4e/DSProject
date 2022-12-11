import re

fail = open('aadressid.txt', encoding = 'UTF-8')

for rida in fail:
    nimi = re.search('ut\.ee/~(\w+)', rida)
    if nimi != None:
        print(nimi.group(1))