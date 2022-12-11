#Hinna ja aastate sisestamine 
#hind = float(input("Hind: "))
#aastad = int(input("Vanus: "))
#Auto hinna definitsioon
def auto_hind(hind, aastad):
    #Kui aastad on vordsed 0-ga, siis katkesta rekursioon
    if aastad == 0:
        return round(hind, 2)    
    #Arvuta auto uus hind peale aastaid
    else:
        uus_hind = hind
        uus_hind = round(uus_hind * (1 -(20/100)) ,2)
        #Rekursioon
        return auto_hind(uus_hind, aastad-1)
    #Väljasta vastus   
#print(str(auto_hind(hind, aastad)))
    
