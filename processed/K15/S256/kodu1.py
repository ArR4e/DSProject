import re
fail = open("aadressid.txt", "rt", encoding = "UTF-8")

for rida in fail.readlines():
    rida = rida.strip()
    if re.match("http:\/\/www.ut.ee\/~.*?\/.*",rida):
        rida = rida.split("~")
        sõne = rida[1].split("/")
        
        print(sõne[0])
        
fail.close()