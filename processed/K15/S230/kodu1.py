import re
f=open("aadressid.txt")
print("Kasutajanimed on:")
for i in f:
    if re.search("http://www.ut.ee/~",i) and not re.search("http://www.ut.ee/~ ",i):
        nimi = re.search("/~(\w+)/", i)
        print(nimi.group(1))