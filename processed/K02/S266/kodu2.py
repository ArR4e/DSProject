from math import*

pikkus = int(input("Sisestage liini pikkus meetrites: "))
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

if pikkus / kaugus == int(pikkus / kaugus):
    postide_vahed = pikkus / kaugus
    
else:
    postide_vahed = int(pikkus / kaugus) + 1

postid = postide_vahed + 1

print(int(postid))