pikkus=int(input("Kui pikk peaks elektriliin olema (täismeetrites)? "))
kaugus=int(input("Kui suur on kõrvuti asetsevate postide vahe (täismeetrites)? "))
poste=round(pikkus//kaugus,0)
if pikkus<=kaugus:
    print("Sel juhul on vaja 2 posti!")
elif (pikkus/kaugus-int(poste))==0:
    print("sel juhul on vaja",poste+1,"posti!")
else:
    print("Siis on vaja",poste+2,"posti!")


#selleks, et kontrollida, kas "poste" komakoht on 0 lahutasin pikkuse/kaugusest sama jagatise ümarduse
#https://www.codegrepper.com/code-examples/python/how+to+check+if+number+has+decimals+python

#kontrollimisel abiks
#p_pikkus=poste*kaugus
#print(pikkus/kaugus)
#print(poste)
#print(p_pikkus)