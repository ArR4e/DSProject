#test5
import re

f = open("aadressid.txt", "r")

pikkus = len("http://www.ut.ee/~")
for i in f:
    a = i.strip()
    lugeja = 0
    
    if re.match("http://www.ut.ee/~", a):
        sõne = ""
        for tähed in a:
            lugeja += 1
            if lugeja > pikkus:
                if tähed == "/":
                    break
                sõne += tähed
        print(sõne)