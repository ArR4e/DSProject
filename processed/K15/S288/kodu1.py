import re

def kasutajanimed(read):
    for i in read:
        if re.match('http://www.ut.ee/~[a-z]', i.strip()):
            i = (re.sub(r'^.*?~', '', i.strip()))
            print(re.sub(r'/.*', '', i))

with open('aadressid.txt', encoding = 'UTF-8') as f:
    read = f.readlines()
    
print('Kasutajanimed on:')

kasutajanimed(read)