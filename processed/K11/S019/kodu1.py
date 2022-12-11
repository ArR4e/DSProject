

def seosta_lapsed_ja_vanemad(f3, f4):
    f1 = open(f3)
    f2 = open(f4, encoding = "UTF-8")
    a = {}
    #b = {}
    lapsed = {}
    vanemad = {}
    for rida in f1:
        vanem, laps = rida.strip().split(" ")
        for rida2 in f2:
            kood, nimi = rida2.strip().split(" ",1)
            #b[kood] = nimi
            if laps == kood:
                lapsed[kood] = nimi
                #a[nimi] = b[vanem]
            if vanem == kood:
                vanemad[kood] = nimi
                print(vanemad)
    f1.close()
    f1 = open(f3)
    for rida in f1:
        vanem, laps = rida.strip().split(" ")
        a[lapsed[laps]] = vanemad[vanem]
    return a        
                
    
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

print(sõnastik)
#print{vanemad)