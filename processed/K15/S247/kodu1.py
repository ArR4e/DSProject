import re

with open("aadressid.txt", encoding = "UTF-8") as f:
    for rida in f:
        for õiged in re.finditer("http://www.ut.ee/~(?:[a-z]|[0-9])+/", rida):
            kasutajad = õiged.group().split("~")
            print(kasutajad[-1].strip("/"))