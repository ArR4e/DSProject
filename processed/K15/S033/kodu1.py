import re
f = open("aadressid.txt", encoding = "latin1")

print("Kasutajanimed on:")
for rida in f:
    rida = rida.strip()
    a = re.match("http://www.ut.ee/~", rida)
    if a:
        b = re.search("~(.*)/", rida)
        print(b.group(1))
        
f.close()