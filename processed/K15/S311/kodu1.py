import re

f = open("aadressid.txt")

olemas = []
for l in f:
    l = l.strip()
    if re.match("http://www.ut.ee/~,*", l):
        nimi = l[18:18+l[18:].index("/")]
        olemas.append(nimi)
f.close
if len(olemas)==0:
    print("Nimesid ei leitud")
else:
    print("Nimed on: ")
    for i in olemas:
        print(i)