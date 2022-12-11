import re

def kasutajanimed(fail):
    f = open(fail, encoding = 'utf-8')
    read= f.readlines()
    f.close()
    for rida in read:
        if re.search('ut.ee/~', rida):
            var = re. search('~(\w+)/', rida)
            print(var.group(1))
            
print('Kasutajanimed on: ')
kasutajanimed('aadressid.txt')