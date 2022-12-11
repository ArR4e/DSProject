import re
f = open("aadressid.txt")
while True:
    rida = f.readline()
    if rida == "":
        break
    if re.search("www.ut.ee", rida):
        if re.search("koit", rida):
            print("koit")
        elif re.search("vilo", rida):
            print("vilo")
        elif re.search("kiho", rida):
            print("kiho")
f.close()