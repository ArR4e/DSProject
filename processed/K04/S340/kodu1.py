from math import pi

def koogi_hind(kooginimi, mõõt):
    if kooginimi == a_kooginimi:
        return a * ((pi * (mõõt**2))/2)
    elif kooginimi == b_kooginimi:
        return b * ((pi * (mõõt**2))/2)
    elif kooginimi == c_kooginimi:
        return c * (mõõt*mõõt)
    
a = 0.06
b = 0.04
c = 0.10

a_kooginimi = "šokolaadikook"
b_kooginimi = "ploomikook"
c_kooginimi = "Napoleoni kook"

kooginimi = input("Palun kirjutage nimetavas käändes kook, mida soovite tellida: ")
mõõt = float(input("Millise raadiuse või küljepikkusega kooki soovite tellida(sentimeetrites): "))
if kooginimi == a_kooginimi or kooginimi == b_kooginimi or kooginimi == c_kooginimi:
    print("Teie tellimus läheb maksma ", str(round(koogi_hind(kooginimi,mõõt),2)), "eurot.")
else:
    print("Sellist kooki andmebaasist ei leitud")