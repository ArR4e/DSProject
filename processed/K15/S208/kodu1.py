import re
fail = open("aadressid.txt", encoding="utf-8")
for rida in fail:
    if re.search("ut.ee/~", rida):
        var = re.search("~(\w+)/", rida)
        if var != None:
            print(var.group(1))
fail.close()
