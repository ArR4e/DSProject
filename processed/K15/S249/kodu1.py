import re

fail = open("aadressid.txt", encoding="utf-8")

def leiame():
    for rida in fail:
        puhas = rida.strip()
        muster = "http://www.ut.ee/~(\d+)/"
        otsi = re.search(muster, puhas)
        print(otsi)



print(leiame())