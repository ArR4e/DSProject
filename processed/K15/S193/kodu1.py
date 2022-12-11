import re
fail = open("address.txt", encoding = "utf-8")

test = "http://www.ut.ee/~vilo/*"

for rida in fail:
    link = re.search(test , rida)
    if link:
        print(link.group(1))

fail.close()