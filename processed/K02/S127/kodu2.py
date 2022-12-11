liini_pikkus=int(input("Sisesta liini pikkus meetrites: "))
postide_kaugus=int(input("Sisesta kahe kõrvuti asetseva posti vaheline maksimaalkaugus meetrites: "))
if postide_kaugus>liini_pikkus:
    poste_vaja=int(2)
if liini_pikkus%postide_kaugus==0:
    poste_vaja=int(liini_pikkus/postide_kaugus+1)
if liini_pikkus%postide_kaugus>0:
    poste_vaja=int(liini_pikkus//postide_kaugus+2)  
print("Liini ehitamiseks on minimaalselt vaja " + str(poste_vaja) + " posti.")