import re
f=open("aadressid.txt")
m=f.readlines()
f.close()

print("Kasutajanimed on:")
for x in m:
    x=x.strip()
    if re.match("http://www.ut.ee/~",x):
        x=x.strip()
        l=x[17:].index("/")
        print(x[18:(l+17)])
        
        
