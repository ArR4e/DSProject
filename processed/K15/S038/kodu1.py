import re

fail = open("aadressid.txt",encoding="utf-8")

muster = r"ut[.]ee/~(\w+)"


print("Kasutajanimed on: ")
for line in fail:
    vaste = re.search(muster, line)
    if vaste != None:
        uus = vaste.group()
        uuem = uus.split("~")
        print(uuem[1])
        

        