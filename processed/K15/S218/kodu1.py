import re

print("Nimed on: ")
with open("aadressid.txt", encoding="utf-8") as f:
     for rida in f:
         nimi = re.search("http://www.ut.ee/~([A-Za-z_0-9.-]+).*", rida)
         if nimi:
             print(nimi.group(1))
            