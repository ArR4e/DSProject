import re
fail = open("aadressid.txt", encoding="utf-8")

for rida in fail:
    if re.search("www.ut.ee/~", rida):
        var = re.search("www.ut.ee/~(\w+)/", rida)
        print(var.group(1))