import re

fail = open("aadressid.txt", "r")
print("Kasutajanimed on:")
for rida in fail:
    x = re.search(r"http://www.ut.ee/~(\w+)/", rida)
    if x is not None:
        print(x.group(1))