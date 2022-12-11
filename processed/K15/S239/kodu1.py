import re

f=open("aadressid.txt",encoding="UTF-8")

print("Kasutajanimed on: ")

for rida in f:
    rida=rida.split("/")
    if len(rida)>1:
        if rida[2]=="www.ut.ee":
            if re.search("~",rida[3][0]):
                print(rida[3][1:])

f.close()