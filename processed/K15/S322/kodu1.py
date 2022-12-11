import re
print("Kasutajanimed on:")
with open("aadressid.txt", "r") as fail:
    for rida in fail:
        if re.match("http://www.ut.ee/~*", rida):
            print(rida.split("/")[3][1:])
