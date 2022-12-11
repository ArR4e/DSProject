import re
f=open("aadressid.txt")
print("Kasutajanimed on:")
for rida in f:
    if re.search("www.ut.ee/[~][a-z]", rida):
        järjend=rida.split("/")
        print(järjend[3].replace("~", ""))
        
    