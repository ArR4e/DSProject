#programm küsib sisendit
liini_pikkus = int(input("Sisestage liini pikkus (täisarvuna meetrites): "))
maksimaalkaugus = int(input("Sisestage Kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
#defineeritakse muutuja, mille abil jälgitakse minimaalset postide arvu
postid = 1

#iga tsükliga lahutatakse kogu liini pikkusest maha üks maksimaalkaugus ja selle arvelt ehitatakse üks post juurde
#kestab niikaua, kuni liini on maksimaalkaugusest vähem
while liini_pikkus > maksimaalkaugus:
    postid+=1
    liini_pikkus-=maksimaalkaugus

#kui liin ei moodustu ainult maksimaalkaugustest, liidetakse postide arvule 1 juurde, et arvestada viimase liinilüliga, millega varem ei arvestatud
if liini_pikkus > 0:
    postid+=1

#programm väljastab minimaalse postide arvu
print("Liini ehitamiseks on minimaalselt vaja", postid, "posti.")