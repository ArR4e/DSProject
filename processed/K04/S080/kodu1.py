a="Napoleoni"
b = "Šokolaadi"
c= "Ploomi"
d = 0.1
e = 0.04
f = 0.06
from math import (pi)
def koogi_hind(kooginimi,mõõt1):
    if kooginimi == "šokolaadikook":
        return(round((((pi)*mõõt1**2)*f),2))
    elif kooginimi == "Napoleoni kook":
        return(round(((mõõt1**2)*d),2))
    elif kooginimi == "ploomikook":
        return(round((((pi)*mõõt1**2)*e),2))
    else:
        raise Exception ('Sellist kooki ei ole')
    
while True:
    kooginimi=input("Sisesta koogi nimi: ")
    if kooginimi == "":
        #g=(kooginimi[0]).upper()
        #kooginimi=(kooginimi[0]).replace(kooginimi[0],g)+kooginimi[1:(len(kooginimi))]
    
        break
    mõõt1 = float(input("Sisesta koogi ühe külje pikkus (cm): "))
 
#while kooginimi != "":
    hind = koogi_hind(kooginimi,mõõt1)
    print(hind)
    