#Pagarikoja kassaaparaat

from math import *
def koogi_hind(nimi,mõõt):
    my_dict = {"šokolaadikook": 0.06,
               "ploomikook": 0.04,
               "napoleoni kook": 0.10}
    nimi = nimi.lower()
    
    #kuidas seda tööle saada
    if my_dict.get(nimi)== None:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    if nimi == "napoleoni kook":
        summa = round(my_dict[nimi]*mõõt**2,2)
        print(summa)
        return summa
    else:
        #ringi kujuline
        if nimi in my_dict:
            summa= round( ((my_dict[nimi])*((pi))*(mõõt)**2),2)
            print(summa)
            return summa
            
        
            
            
while True:
    a = str(input("Sisestage koogi nimi:"))
    if a == "" or a ==" ":
        break
    b = float(input("Sisestage koogi mõõtmed:"))
    koogi_hind(a,b)
