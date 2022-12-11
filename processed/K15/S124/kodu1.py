import re
f = open('aadressid.txt', encoding = 'utf-8')
try:
    for rida in f:
        if re.search('www.ut.ee', rida):
            if re.search("[~]", rida):
                nime_osa = re.search("/~\w+/", rida)
                nime_osa = nime_osa.group()
                match = re.search("\w+", nime_osa)
                nimi = match.group()
                print(nimi)
except:
    pass
       
f.close()   
    