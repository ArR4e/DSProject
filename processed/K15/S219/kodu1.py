import re
f = open("aadressid.txt", "r")

print("Kasutajanimed on:")
for rida in f:
    rida = rida.strip()
    if re.match("http://www.ut.ee/~",rida):
        väiksemrida = rida[18:]
        print(väiksemrida.split('/')[0])
        
f.close()