import re
fail = open('aadressid.txt', 'r', encoding='utf-8')

for rida in fail:
    for sobiv in re.finditer('http://www.ut.ee/~(?:[a-z]|[0-9])+/', rida):
        jar = sobiv.group().split('~')
        print(jar[-1].strip('/'))