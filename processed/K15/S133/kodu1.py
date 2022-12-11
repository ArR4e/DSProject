import re
aad=open("aadressid.txt",encoding="UTF-8")
a=[]

for rida in aad:
    n=[]
    #print(rida)
    if re.search("http://www.ut.ee/~",rida):
        s=rida.split("/")
        i=s.index("www.ut.ee")
        n=s[i+1]
        n=n.replace("~","")
    if " " in n:
        continue
        
    elif len(n)!=0:
        a+=[n]
if len(a)!=0:
    print("Kasutajanimed on:")
    for r in a:
        print(r)
        