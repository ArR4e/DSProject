import re

def printer(link):
    i = link.index("~")
    link = link[i+1:]
    n = link.index("/")
    link = link[:n]
    return link

with open("aadressid.txt", "r", encoding="UTF-8") as f:
    for rida in f:
        if re.search("www.ut.ee/~",rida):
            kasutaja = printer(rida)
            if " " not in kasutaja:
                print(kasutaja)