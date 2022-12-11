import re

fail = open("aadressid.txt", encoding = "utf-8")

a = "http://www.ut.ee/~(\w*)/.*"

for rida in fail:
    link = re.search(a, rida)
    if link:
        print(link.group(1))

    
fail.close()