import re

f=open("aadressid.txt",encoding="utf8")

for aadress in f:
    a=re.search("http://www.ut.ee/~(\w*)",aadress)
    if a:
        print(a.group(1))
        
f.close()