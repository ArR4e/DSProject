import re

fail = open("aadressid.txt","r",encoding="UTF-8")
print("Kasutajanimed on: ")
for rida in fail:
    x = re.findall("http://www.ut.ee/~[^ ]+?/",rida.strip())
    if len(x) > 0:
        print(re.findall("~[^ ]+?/",x[0])[0][1:len(re.findall("~[^ ]+?/",x[0])[0][1:])])