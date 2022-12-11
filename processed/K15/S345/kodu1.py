import re 

f = open("aadressid.txt", encoding="UTF-8")

print("Kasutajanimed on: ")

for rida in f:
    nimi = []
    if rida.strip()[:5] == "http:" and "www.ut.ee" in rida:
        muster = re.compile("~([a0-züäöõ9]*)/")
        if re.search(muster, rida):
            nimi = muster.findall(rida)
            print(nimi[0])

f.close()