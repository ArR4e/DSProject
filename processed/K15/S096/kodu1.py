# 1. regulaaravaldis

import re

f = open("aadressid.txt", encoding="UTF-8")

for rida in f:
    a = rida.strip()
    if re.search("http://www.ut.ee/~[a-zA-Z0-9]*/", a):  #Vaatab kas ut.ee ja nimi on tekstis olemas ja kui on siis prindib nime
        nimi = re.search("~[a-zA-Z0-9]*/", a)
        print(nimi.group()[1:-1])