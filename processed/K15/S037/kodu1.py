import re

f = open('aadressid.txt', 'r')
print("Kasutajanimed on: ")
for rida in f:
    if re.search("http://www.ut.ee/~",rida.strip()):
        kasutajanimi = re.search("http://www.ut.ee/~(\w*)/", rida.strip())
        print(kasutajanimi.group(1))
        
