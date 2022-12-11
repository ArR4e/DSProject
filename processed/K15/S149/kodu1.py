import re

with open("aadressid.txt") as f:
    fail = f.readlines()
print("Kasutajanimed on: ")
re.match("a.i","ai")
for rida in fail:
    if 3 >= rida.find("http://www.ut.ee/~") >= 0:
        print(rida[rida.find("~") + 1 : rida.find("~") + 1 + rida[rida.find("~") + 1:].find("/")])