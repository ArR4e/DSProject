#alustasin 08.12.2021 (16:24)
import re

f = open('aadressid.txt')
for rida in f:
    var = re.search('http://www.ut.ee/~(\w+)/', rida)
    if var:
        print(var.group(1))