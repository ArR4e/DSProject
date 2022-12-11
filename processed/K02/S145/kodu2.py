liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))

if liini_pikkus == maksimaalkaugus:
    postide_arv_liinil = str(int((liini_pikkus/maksimaalkaugus)+1))
    print("Poste on liinil " + postide_arv_liinil)
elif liini_pikkus == 0:
    print("Poste on liinil 0")
elif liini_pikkus >= 1 and maksimaalkaugus == 1:
    postide_arv_liinil = str(int((liini_pikkus/maksimaalkaugus)+1))
    print("Poste on liinil " + postide_arv_liinil)
elif liini_pikkus > maksimaalkaugus or liini_pikkus < maksimaalkaugus:
    postide_arv_liinil = str(int((liini_pikkus/maksimaalkaugus)+2))
    print("Poste on liinil " + postide_arv_liinil)