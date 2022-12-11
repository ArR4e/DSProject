import re

f = open("aadressid.txt")

print("Kasutajanimed on: ")
for rida in f:
    if re.search("\.ee\/~([^~\/\s]+)", rida):
        var = re.search("\.ee\/~([^~\/\s]+)", rida)
        print(var.group(1))
    else:
        continue
f.close()