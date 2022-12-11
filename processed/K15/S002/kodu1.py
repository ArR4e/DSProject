import re

fail = open("aadressid.txt","r",encoding="utf-8")
tekst = fail.read()
fail.close()

otsing = "h.*e/~.*/"
nimed = re.findall(otsing, tekst)

for i in nimed:
    print(i.split("/")[3][1:])
