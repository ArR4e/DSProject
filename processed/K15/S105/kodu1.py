import re

f = open("aadressid.txt", "r")
nimed=[]
for rida in f:
    x = re.search("http://www.ut.ee/~[a-z0-9]+/", rida)
    if x != None:
        y = re.search("~[a-z0-9]+/", rida)
        nimi = re.search("[a-z0-9]+", y.group())
        nimed.append(nimi.group())
f.close()

for nimi in nimed:
    print(nimi)