import re

f = open("aadressid.txt", encoding = "UTF-8")
kasutajanimed = ""
for rida in f:
    if re.match(" *http://www.ut.ee/~.*/", rida):
        järjend = list(rida.split("/"))
        nimi = järjend[3].replace("~","")
        kasutajanimed += "\n" + nimi 
    else:
        continue
f.close()

print("Kasutajanimed on: " + kasutajanimed)
