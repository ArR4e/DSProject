import re
f = open("aadressid.txt", "r", encoding= "UTF-8")
for rida in f:
    match = re.search(r'://www.ut.ee/~([\w.-]+', rida)
    if match:
        print(match.group(1))