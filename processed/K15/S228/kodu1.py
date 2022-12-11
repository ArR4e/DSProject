import re

fail = open('aadressid.txt', encoding = 'UTF-8')

for rida in fail:
    otsitav = re.search('http://www.ut.ee/~(\w+)/', rida) 
    if otsitav: #kui leitakse otsitav regulaaravaldis, siis tulemuseks True -> täidab if haru 
        print(otsitav.group(1)) #nimi on grupeeritud, sulgudes, seda saab kätte käsuga 'group'

fail.close()