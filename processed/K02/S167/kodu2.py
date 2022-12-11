#elektriliin

#Sirgjoonelise elektriliini ehitamisel paigutatakse kõrvutiasetsevad postid võrdsete kaugustega, mis ei ületa etteantud maksimaalkaugust.
#Liin algab ja lõpeb postiga.
#Kasutajalt küsitakse liini pikkust (täisarvudena meetrites) ja kõrvutiasetsevate postide maksimaalkaugust (täisarvuna meetrites).
#Ekraanile väljastatakse, mitu posti on liini ehitamiseks minimaalselt vaja.


liinikaugus = int(input(print("Mis on elektriliini liinipikkus meetrites?")))

max_postide_kaugus = int(input(print("Mis on postidevaheline kaugus meetrites?")))

min_postide_arv_baasarv = int(round((int(liinikaugus)/int(max_postide_kaugus))))

min_postide_arv = int((int(min_postide_arv_baasarv) + 1))
#kui on tavaline postijada
min_postide_arv2 = int((int(min_postide_arv_baasarv) + 2))
#kui on jäägiga liinikaugus
min_postide_arv3 = 2
#alati on kaks posti, mistahes kaugusel

if int(liinikaugus) < int(max_postide_kaugus):
    print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv3))
elif int(liinikaugus) > (int(min_postide_arv_baasarv)*int(max_postide_kaugus)):
    print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv2))
else: print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv))