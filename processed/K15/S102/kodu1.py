import re
f=open('aadressid.txt')
for rida in f:
    if re.match('http://www.ut.ee/~.+/', rida.strip()):
        print(rida.split('/')[3][1:])