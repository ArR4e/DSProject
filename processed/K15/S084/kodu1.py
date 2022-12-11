import re
print("Kasutajanimed on: ")
with open("aadressid.txt") as f:
    for i in f.readlines():
        i = i.strip()
        if re.match("http://www.ut.ee", i):
            i = i.split("/")
            for j in i:
                if "~" in j:
                    print(j.replace("~",""))