import re

sample = 'http://www.ut.ee/~([a-zA-Z0-9]+)/'
print('Kasutajanimed on:')
with open('aadressid.txt') as f:
    for line in f:
        temp = re.search(sample, line)
        if temp:
            print(temp.group(1))
