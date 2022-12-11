import re

fail = open("aadressid.txt", encoding = "UTF-8")
print("Kasutajanimed on:")

for rida in fail:
    if re.search("www.ut.ee/~[a-zõäöü]", rida):
        rida = rida.split("/")
        for sümbol in rida:
            if "~" in sümbol:
                print(sümbol[1:])
                
fail.close()
