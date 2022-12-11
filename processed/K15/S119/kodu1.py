import re

print("Kasutajanimed on:")

f = open("aadressid.txt", "r")
for rida in f:
    jarj = rida.split("/")
    kasutaja = r"^~\w+$"
    if "www.ut.ee" in jarj:
        for el in jarj:
            if re.match(kasutaja,el):
                muster = r"\~"
                el = re.sub(muster,"",el)
                print(el)
f.close()