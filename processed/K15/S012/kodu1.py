#kodu 1 - regulaaravaldis
import re
f = open("aadressid.txt")
for rida in f:
    y = re.search("http://www.ut.ee", rida)
    x = re.search("\/~\w+/", rida)
    if x and y:
        print(x.group().replace("~", "").strip("/"))
f.close()
