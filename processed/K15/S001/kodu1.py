import re

fail = open("aadressid.txt", "r", encoding="utf-8")

for rida in fail:
    rida = rida.strip()
    if re.match("http://www.ut.ee/~", rida):
        rida = rida.split("~")
        rida[1] = rida[1].split("/")
        print(rida[1][0])

fail.close()