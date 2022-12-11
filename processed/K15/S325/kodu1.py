import re
a=[]
f=open("aadressid.txt")
for line in f:
    if re.match("http://www.ut.ee/~",line.strip()):
        a+=[line]
if a!=[]:
    print("Kasutajanimed on:")
    for elem in a:
        x=elem.split("/")
        for i in x:
            if "~" in i:
                print(i.strip("~"))
f.close()