import re
f = open("aadressid.txt","r",encoding = "UTF-8")

print("Kasutajanimed on: ")
for rida in f:
    rida = rida.replace("\n","")#.replace(".","")
    if re.search("[.]ee.~",rida):
        sõne = re.findall("ee.~[a-z]*[0-9]*[a-z]*[0-9]*",rida)
        if len(sõne) > 0:
            sõne = sõne[0].replace("ee/~","")
            print(sõne)

f.close()

