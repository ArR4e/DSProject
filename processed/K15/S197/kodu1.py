import re
with open('aadressid.txt', 'r', encoding='utf-8') as f:
    usernames = re.findall('http://www.ut.ee/~(\S*?)/', str(f.readlines()))
print('Kasutajanimed on:')
print(*usernames, sep='\n')