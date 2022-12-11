import re

with open("aadressid.txt") as f:
    print("Kasutajanimed on:")
    for i in f.readlines():
        i = re.findall("ut\\.ee/~[^ ]+/", i)
        if i != []:
            noUTee = re.sub("ut.ee/~", "", i[0])
            noChildPage = re.sub("/.*", "", noUTee)
            print(noChildPage)
