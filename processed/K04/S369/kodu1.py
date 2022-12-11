from math import pi

def ringi_pindala(raadius):
    return pi * raadius**2

kook1 = float(0.06)
kook2 = float(0.04)
kook3 = float(0.10)

def koogi_hind(nimi, s):    
    if nimi == "šokolaadikook":
        pindala = ringi_pindala(s)
        hind = pindala * kook1
        return round(hind, 2)
    
    if nimi == "ploomikook":
        pindala = ringi_pindala(s)
        hind = pindala * kook2
        return round(hind, 2)
        
    if nimi == "Napoleoni kook":
        pindala = s * s
        hind = pindala * kook3
        return round(hind, 2)
    
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        
    
def main():
    while True:
        try:
            koogi_nimi = input("Sisestage koogi nimi: ")
            if koogi_nimi == "":
                break
            koogi_suurus = float(input("Sisestage koogi suurus: "))
            
            print(koogi_hind(koogi_nimi, koogi_suurus))
        except Exception as e:
            print(e)
main()


        
        

