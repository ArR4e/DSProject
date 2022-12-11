#Elektriliin

liini_pikkus = int(input("Sisestage liini pikkus meetrides:"))
postide_vahe = int(input("Sisestage kõrvutiasestsevatepostide maksimaalkagus meetrides:"))

def liinid_ja_kogus(liini_pikkus,postide_vahe):
    summa = 0
    if liini_pikkus <= postide_vahe:
        return 2
    else:
        if postide_vahe == 1:
            return  liini_pikkus + 1
        else:
            return (liini_pikkus//postide_vahe + 2)

print(liinid_ja_kogus(liini_pikkus,postide_vahe))

