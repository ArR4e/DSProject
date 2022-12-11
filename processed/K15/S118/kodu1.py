import re

fail = open("aadressid.txt", "r", encoding="utf-8")

print("Kasutajanimed on:")

for rida in fail.readlines():
    if re.search("~.*/", rida):
        if  re.match("^ *http://www.ut.ee/.*", rida):
            print(rida.split("~")[-1].split("/")[0])

fail.close()