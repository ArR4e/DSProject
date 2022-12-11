import re

fail = "aadressid.txt"
avafail = open(fail)

for rida in avafail:
    if re.search("http://www.ut.ee/~", rida):
        rida = rida.strip().split("/")
        nimi = rida[3].split("~")
        pärisnimi = nimi[1]
        print(pärisnimi)
        