import re

f = open("aadressid.txt")

print("Kasutajanimed on:")
for rida in f:
    kasutajanimi = re.search("http://www.ut.ee/~(\w+)/", rida)
    if kasutajanimi:
        print(kasutajanimi.group(1))

    
f.close()