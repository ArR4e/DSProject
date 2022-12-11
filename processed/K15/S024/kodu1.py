import re

f = open("aadressid.txt", encoding="UTF-8")

for rida in f:
    if re.match("http://www.ut.ee/~", rida):
        jar = re.split("/", rida)
        kasutajanimi = jar[3].strip("~") 
        print(kasutajanimi)

f.close()