import re
with open('aadressid.txt', encoding='UTF-8') as file:
    link = r'http://www.ut.ee/~(\w*)/.*'
    for rida in file:
        x = re.search(link, rida)
        if x:
            print(x.group(1))