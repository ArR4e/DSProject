import re
print("Kasutajanimed on: ")
f = open('aadressid.txt', encoding = 'utf-8')
for rida in f.readlines():
    if re.search('ut-ee/~', rida):
        var = re.search('~(\w+)/', rida)
        print(var.group(1))
