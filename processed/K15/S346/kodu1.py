import re

f = open("aadressid.txt")
for rida in f:
    i = rida
    http = re.search("http", i)
    if http:
        nimi = re.search("ee/~(\w+)/", i)
        if nimi:
            print(nimi.group(1))