import re

with open('aadressid.txt') as f:
    print('Kasutajanimed on:')
    for line in f:
        if re.search('ut\.ee/~[^ ]', line):
            line = line.strip().split('/')
            for el in line:
                if '~' in el:
                    print(el[1:])
        else:
            continue