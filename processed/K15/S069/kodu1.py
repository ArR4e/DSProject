import re
f = open('aadressid.txt')
print('Kasutajad on:')
for line in f:
    if re.search('.*ut\.ee/~([a-z].*)/', line):
        x = re.search('.*ut.ee.*.~(.*?)/', line)
        print(x.group(1))
f.close()