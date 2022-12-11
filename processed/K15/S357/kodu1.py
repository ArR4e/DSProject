import re

f = open("aadressid.txt")
lingid = []
for line in f:
    line = line.strip()
    lingid.append(line)
print("Kasutajanimed on:")
for el in lingid:
    if re.match("http://www.ut.ee/~.*/", el):
        vahemik = re.search("~.*/", el).span()
        kasutaja = el[vahemik[0] +1: vahemik[1] -1]
        if "/" in kasutaja:
            i = kasutaja.index("/")
            print(kasutaja[0: i])
        else:
            print(kasutaja)