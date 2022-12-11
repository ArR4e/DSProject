# parandatud hiljem

liinipikkus = (int(input("Sisestage liini pikkus meetrites: ")))
maksimaalkaugus = (int(input("Sisestage postide maksimaalkaugus: ")))

if liinipikkus <= maksimaalkaugus:
    elektripostid = 2
if liinipikkus == 1:
    elektripostid = 2
else:  
    elektripostid = liinipikkus / maksimaalkaugus + 2
print(round(elektripostid))