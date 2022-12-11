import re

fail = open("aadressid.txt")
for i in fail.readlines():
    try:
        vahe=i.split("/~")
        vahe2=vahe[1].split("/")
        nimi=vahe2[0]
        if re.search(nimi,i):
            if re.search("www.ut.ee",i):
                print(nimi)
    except:
        None
fail.close()