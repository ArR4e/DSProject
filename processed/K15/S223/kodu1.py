import re
with open('aadressid.txt', 'r', encoding='utf8') as f:
    list_rows = [x.strip() for x in f.readlines()]
print('kasutajanimed on:')
for x in list_rows:
    if re.match("http://www.ut.ee/~", x):
        print(x[x.index('~')+1:x.index('/',x.index('~')+1)])