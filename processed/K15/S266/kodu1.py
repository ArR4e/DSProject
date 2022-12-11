#regulaaravaldis
import re
fail = open('aadressid.txt', 'r', encoding = 'UTF-8')

print('Kasutajanimed on:')
for rida in fail:
    m = re.search(r'.*www.ut.ee/~([a-z0-9A-Z_]+)/.*', rida)
    if m:
        print(m.group(1))