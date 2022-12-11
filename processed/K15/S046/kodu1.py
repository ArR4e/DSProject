import re
f = open("aadressid.txt","r",encoding="utf-8")
print("Kasutajanimed on:")
for rida in f:
    match = re.search(r'://www.ut.ee/~([\w.-]+)', rida)
    if match:
        print(match.group(1))
f.close()
