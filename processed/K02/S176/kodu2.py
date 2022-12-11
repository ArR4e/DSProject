import time

print("Ehitatakse elektriliin, mille postid paigutatakse võrdsete kaugustega ning \
ei ületa teie poolt antud maksimaalkaugust")
time.sleep(3)

pikkus = int(input("Sisestage liini pikkus täisarvuna meetrites: "))
kaugus = int(input("Sisestage maksimaalne postide vahe täisarvuna meetrites: "))

minimaalne_postide_arv = int(pikkus / kaugus + 1)
#liidame ühe, sest muidu jääks üks post kas liini algusest või lõpust puudu
print("Liini ehitamiseks on minimaalselt vaja " + str(minimaalne_postide_arv) + " posti")
# kasutaja saab teada minimaalse postide arvu
if kaugus < pikkus:
    print("Jargmiseks vali soovitud postide arv")
else:
    print("Liini pikkus on väiksem kui kahe posti vahe")
    exit()
postid = int(input("Sisestage elektripostide arv: "))
if postid > minimaalne_postide_arv:
    print("Postide kaugus üksteisest on: " + str(pikkus / postid))
elif postid < minimaalne_postide_arv:
    print("Postide vahe ületab maksimaalse kauguse!")
else:
    print("Postide kaugus on esialgselt maaratud maksimaalne kaugus")