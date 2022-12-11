from math import pi

def koogi_hind(k_nimi, k_mõõdu):
    if k_nimi.lower() == "šokolaadikook":
        return(round((pi * k_mõõdu ** 2 * 0.06), 2))   
    elif k_nimi.lower() == "ploomikook":
        return(round((pi * k_mõõdu ** 2 * 0.04), 2))    
    elif k_nimi.lower() == "napoleoni kook":
        return round((k_mõõdu ** 2 * 0.10), 2)    
    else:
        print("Sellist kooki andmebaasist ei leitud")


while True:
    k_nimi = str(input("Sisetage koogi nime: "))
    if k_nimi == "":
        break
    k_mõõdu = float(input("Teie koogi mõõdu(koogi raadius): "))
    print(koogi_hind(k_nimi, k_mõõdu))
