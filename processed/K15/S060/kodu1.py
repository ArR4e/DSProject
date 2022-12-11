f=open("aadressid.txt","r")
import re
a=[]
for rida in f:
    if re.search("://www.ut.ee/~[a-z]",rida):
        l=rida.split("~")
        v=l[1].split("/")
        a.append(v[0])
print("Kasutajanimed on:")
for rida in a:
    print(rida)
        