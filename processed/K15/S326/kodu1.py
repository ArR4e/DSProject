import re

fail = open("aadressid.txt")
print("Kasutajanimed on: ")
for rida in fail:
    if re.search("ut[.]ee", rida):
        nimi = re.search("ee/~(\w+)/", rida)
        if nimi != None:
            print(nimi.group(1))