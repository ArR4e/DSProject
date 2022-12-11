import re

f = open("aadressid.txt")

for rida in f:
    rida = rida.strip()
    if re.match("http://www.ut.ee/~", rida):
        rida = re.sub("http://www.ut.ee/~","",rida)
        rida = re.sub("/.*","",rida)
        print(rida)
        