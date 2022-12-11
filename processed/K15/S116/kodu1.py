fail = open("aadressid.txt" , "r", encoding="UTF-8")
import re

print("Kasutajanimed on: ")

while True:
    rida = fail.readline()
    rida = rida.strip()
    if rida == "":
        break
    if re.match("^http://www.ut.ee/~", rida):
        nimi = rida.split("/")[3][1:]
        print(nimi)
        
fail.close()