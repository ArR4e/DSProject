import re
print('Kasutajanimed on:')
with open('aadressid.txt')as f:
    for rida in f:
        for match in re.finditer('http://www.ut.ee/~(?:[a-z]|[0-9])+/', rida):
            järjend=match.group().split('~')
            print(järjend[-1].strip('/'))