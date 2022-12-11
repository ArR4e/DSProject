import math
koogid= {
    "šokolaadikook":0.06, #ring, raadius
    "ploomikook": 0.04, #ring raadius
    "napoleoni kook": 0.10 #ruut kuljepikkus
}
go=True

def koogi_hind(n,m):
    hind= 0
    if n == "šokolaadikook" or n == "ploomikook":
        hind= math.pi*(m**2)
    else:
        h=m**2
    return round(h,2)

while go == True:
    nimi= str(input("koogi nimi : ")).lower()
    if nimi == "":
        go= False
    else:
        if nimi in koogid:
            moot= float(input("koogi moot: "))
            print("koogi hind on:" + str(koogi_hind(nimi,moot)))
        else:
            print("sellist kooki andmebaasist ei leitud")