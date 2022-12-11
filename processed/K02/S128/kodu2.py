#Elektriliin
#Sirgjoonelise elektriliini ehitamisel paigutatakse kõrvutiasetsevad postid võrdsete kaugustega, mis ei ületa etteantud maksimaalkaugust.
#Liin algab ja lõpeb postiga. Kasutajalt küsitakse liini pikkust (täisarvuna meetrites) ja kõrvutiasetsevate postide maksimaalkaugust (täisarvuna meetrites).
#Ekraanile väljastatakse, mitu posti on liini ehitamiseks minimaalselt vaja.
import math
liini_pikkus = int(input("Mis on liini pikkus?: "))
maksimaalkaugus = int(input("Mis on kõrvutiasetsevate postide vaheline maksimaalkaugus?: "))
postide_arv = math.ceil(liini_pikkus / maksimaalkaugus + 1) #Jagades liini pikkuse vahede maksimaalkagusega saame vahede arvu. Vahesid alati ühe võrra vähem kui poste.
print(postide_arv)