import re
from datetime import datetime
fail = input('Sisesta faili nimi: ')
f = open(fail)
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
ajad = []
raha = []
for line in f:
    x = re.search('(..:..?).(..:..?).(.?)', line)
    start = datetime.strptime(x.group(1), '%H:%M')
    end =   datetime.strptime(x.group(2), '%H:%M')
    diff = end - start
    diff_in_hours = diff.total_seconds() / 3600
    ajad.append(diff_in_hours)
    try:
        k = int(x.group(3))
        raha.append(k)
    except:
        continue
f.close()
aegv = []    
kaua = max(ajad)
for el in range(len(ajad)):
    if ajad[el]<kaua:
        aegv.append(el)
rahav = []
palju = max(raha)
for el in range(len(raha)):
    if raha[el]<palju:
        rahav.append(el)
vastus = []   
for el in aegv:
    if el in rahav:
        vastus.append(el)
f = open(fail)
sisu = f.readlines()
for el in vastus:
    print(sisu[el].strip())
        
        
        