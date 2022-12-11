import re

print("Kasutaja nimed on:")
with open("aadressid.txt", encoding="utf-8") as f:
    for i in f:
        i = i.strip()
        if re.match(r'\bhttp://www.ut.ee/~\b', i):
            i = i.replace('http://www.ut.ee/~','').split("/")
            print(i[0])