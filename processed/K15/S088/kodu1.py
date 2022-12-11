import re

f = open("aadressid.txt", encoding = "utf-8")

print("Kasutajanimed on:")
for i in f:
    i = i.strip()
    l = i.split("/")
    if re.match("http://", i):
        if re.search("http://www.ut.ee/~.*", i):
            print(l[3].strip("~"))
f.close()
