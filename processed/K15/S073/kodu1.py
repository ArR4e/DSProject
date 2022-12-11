import re

with open("aadressid.txt", encoding="UTF-8") as f:
    lines = f.readlines()

reg = "(?<=\/~)[^\/(\n|\s)]*"

print("Kasutajanimed on:")
unames = set()
for i in lines:
    e = re.search(reg, i)
    if e:
        if not e.group(0) in ["eller", "kasutajanimi", "utvee"]:
            unames.add(e.group(0))
        
for i in unames:
    print(i)