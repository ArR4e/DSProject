import re

f = open('aadressid.txt')

print("Kasutajanimed on: ")
for rida in f:
    if re.search("ut[.]ee/~[a-züõöä]", rida):
        rida = rida.split('/')
        for i in rida:
            if '~' in i:
                print(i[1:])