import re
f = open("aadressid.txt", encoding = "UTF-8")
for rida in f:
    if re.search("http[s]?://www.ut.ee/~", rida) and re.match(" *http[s]?", rida):
        nimi = rida.split("~")
        nimi = nimi[1].split("/")[0]
        print(nimi)