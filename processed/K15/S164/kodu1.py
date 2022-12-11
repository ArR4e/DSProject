import re


fail = open("aadressid.txt", encoding = "utf-8")
for rida in fail:
    vaste = re.search("http://www.ut.ee/~(\w+)", rida)
    if vaste:
        print(vaste.group(1))
        
        
    
