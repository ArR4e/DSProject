import re
f=open("aadressid.txt", encoding="UTF-8")
for rida in f:
    rida2=rida.split("/", 4)
    try:
        if re.search("http://www.ut.ee/", rida):
            if re.search("~[a-y]", rida):
                rida3uus=rida2[3].split("~")
                if rida3uus[0]=="":
                    print(rida3uus[1])
            
    except:
        continue
        
f.close()