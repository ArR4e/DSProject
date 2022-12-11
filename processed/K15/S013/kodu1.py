import re
fail = open("aadressid.txt")
print("Kasutajanimed on:")
for rida in fail:
    rida = rida.strip("\n")
    var = re.search("http://www.ut.ee/~(\w+)/", rida)
    if var == None:
        continue
    else:
        print(var.group(1))