import re
with open("aadressid.txt") as f:
    read = f.read().splitlines()
    
print("Kasutajanimed on: ")
for rida in read:
    if re.search('.*ut\.ee/~([a-z].*)/', rida):
        vastus = re.search('.*ut.ee.*.~(.*?)/', rida)
        print(vastus.group(1))
    