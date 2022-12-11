import re

aadressid_fail=open("aadressid.txt", "r")
kasutajanimed=[]

for rida in aadressid_fail:
    
    otsing=re.search("(ht{2}p[:]/{2})(w{3}[.]ut[.]e{2}/~)(\w+).*", rida)
    
    if otsing:
        
        kasutajanimed.append(otsing.group(3))

if kasutajanimed==[]:
    print("Ei leidunud kasutajanimedega aadresse")
else:
    print("Kasutajanimed on: ")
    for el in kasutajanimed:
        print(el)