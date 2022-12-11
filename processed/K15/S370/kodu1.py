import re
f=open("aadressid.txt", "r")

nimed=[]
for line in f:
    line=line.strip()
    if re.match("http://www.ut.ee/~.*", line):
        nimi=line[18:18+line[18:].index("/")]
        nimed.append(nimi)
f.close

if len(nimed)==0:
    print("Kasutajanimesid ei leitud")
else:
    print("Kasutajanimed on:")
    for i in nimed:
        print(i)