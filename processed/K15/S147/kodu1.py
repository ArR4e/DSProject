import re
with open("aadressid.txt",encoding="utf-8") as aadressid:
    sisu = aadressid.read().split("\n")
for rida in sisu:
    if re.match("http://www.ut.ee/~",rida.strip()):
        nimi = rida.replace("//","/").split("/")[2].replace("~","")
        print(nimi)