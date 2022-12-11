import re
a = ['asda']
b = re.match(a[0], '...[c-f]')
with open('aadressid.txt', 'r', encoding = 'UTF-8') as header:
    for i in header:
        if i.strip(' ').startswith('http://www.ut.ee/~'):
            a = i.strip(' http://www.ut.ee/~')
            print(a.split('/')[0])