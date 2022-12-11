import re

f = open("aadressid.txt","r",encoding="utf-8")

print("Kasutajanimed on: ")

while True:
    rida = f.readline()
    
    if rida == "":
        break
    
    rida = rida.strip(" ")
    
    if re.match("http://www.ut.ee/~", rida):
        osad = rida.split("/")
        
        print(osad[3][1:])
f.close()