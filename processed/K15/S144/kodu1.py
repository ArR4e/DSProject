import re

print('Kasutajanimed on: ')
with open('aadressid.txt') as f:
    for i in f:
        if re.match(r'\bhttp://www.ut.ee/~\b', i.strip()):
            i = i.replace('http://www.ut.ee/~','').partition('/')
            print(i[0])