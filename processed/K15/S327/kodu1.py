import re
with open("aadressid.txt", encoding= "utf-8") as f:
    print("Kasutajanimed on: ")
    for rida in f:
        if re.match("http://www.ut.ee/~.", rida.strip()):
            print(rida.split("/")[3].strip("~"))
    