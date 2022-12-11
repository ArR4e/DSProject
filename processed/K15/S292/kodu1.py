import re
nimi = "aadressid.txt"

f = open(nimi, encoding = "utf-8")

for rida in f:
    check = re.findall("\.ut.ee/~[A-Za-z0-9]*/", rida)
    if len(check) != 0:
        k2ik1 = check[0].split("~")
        k2ik2 = k2ik1[1].strip("/")
        print(k2ik2)
    
f.close()