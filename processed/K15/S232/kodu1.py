import re

with open("aadressid.txt", "r+", encoding='utf-8') as f:
    read = f.readlines()
    
kasutajanimed = []
leida = 'http://www\.ut\.ee/~(\w+)/'

for rida in read:
    if re.search(leida, rida):
        kasutajanimi = re.search(leida, rida).group(1)
        kasutajanimed.append(kasutajanimi)

print("Kasutajanimed on: ")
for nimi in kasutajanimed:
    print(nimi)