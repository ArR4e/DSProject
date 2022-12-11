import re

f = open("aadressid.txt")

for rida in f:
    if re.search("[.]ee/~(\w+)/", rida):
        var = re.search("ee/~(\w+)/", rida)
        print(var.group(1))

