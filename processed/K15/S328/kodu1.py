import re

def regex():
    f = open("aadressid.txt", "r")
    aadressid = [line.strip() for line in f]
    f.close()
    
    
    for i in aadressid:
        x = re.findall(r"ut.ee\/\~\w+\/", i)
        if x:
            kasutajanimi = (re.findall(r"~\w+", i))[0]
            print(kasutajanimi[1:])

regex()
    

