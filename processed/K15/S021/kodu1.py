import re

f = open("aadressid.txt", encoding = "UTF-8")
print("Kasutajanimed on:")
for rida in f:
    if re.match(" *http://www.ut.ee", rida):
        tulemus = re.search("~([a-zA-Z0-9]*)/", rida)
        if tulemus != None:
            print(tulemus.group(1))
    else:
        continue