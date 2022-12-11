import re

with open("aadressid.txt", encoding = "UTF-8") as fail:
    read = fail.readlines()
    for rida in read:
        if re.search("www.ut.ee/~",rida):
            for i, täht in enumerate(rida):
                if täht == "~":
                    rida = rida[i+1:]
                    break
            for i, täht in enumerate(rida):
                if täht == "/":
                    rida = rida[:i]
                    break
            if rida[0] != " ":
                print(rida)