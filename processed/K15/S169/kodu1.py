import re

def otsi(avadlis, rida):
    if re.search(avaldis,rida):
        return rida
    else:
        return 0
    
fail = open("aadressid.txt","r",encoding="utf-8")
avaldis = "ut[.]ee/~\w+"
otsitavad = []
for a in fail.readlines():
    if otsi(avaldis,a.strip()) != 0:
        otsitavad.append(a)

print("kasutajanimed on:")
for a in otsitavad:
    print(a.split("/")[3][1:])
    
    