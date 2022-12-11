import re
f=open("aadressid.txt", encoding="UTF-8")

for rida in f:
    rida=rida.strip()
    otsing=re.search("ut\.ee/~([a-z0-9]+?)/", rida)
    if otsing:
        print(otsing.group(1))
        


f.close()