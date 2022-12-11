import re
aadressid = open("aadressid.txt", encoding = "UTF-8")
print("Kasutajanimed on:")
for rida in aadressid:
    b = rida.strip()
    if b.startswith("http://www.ut.ee/~"):
        a = re.search("http://www.ut.ee/~((\w*))/", rida)
        print(a.group(1))
