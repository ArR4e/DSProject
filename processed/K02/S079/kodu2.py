# 2. Elektriliin
# Sirgjoonelise elektriliini ehitamisel paigutatakse kõrvutiasetsevad postid võrdsete kaugustega,
# mis ei ületa etteantud maksimaalkaugust. Liin algab ja lõpeb postiga.
# Kasutajalt küsitakse liini pikkust (täisarvuna meetrites) ja
# kõrvutiasetsevate postide maksimaalkaugust (täisarvuna meetrites).
# Ekraanile väljastatakse, mitu posti on liini ehitamiseks minimaalselt vaja.

# Testi oma programmi!

# Vali vähemalt üks komplekt andmeid nii, et kõik kõrvutiasetsevad postid oleksid maksimaalkaugusel. (Nt liini pikkus 400 m, maksimaalne postidevaheline kaugus 40 m.)
# Vali vähemalt üks komplekt nii, et kõrvutiasetsevad postid oleksid lähemal kui maksimaalkaugus.
# Vali vähemalt üks komplekt, kus liini pikkus oleks postide maksimaalkaugusest väiksem.
# Automaatkontroll. Programm peab küsima kasutajalt täpselt kahte arvu ja kirjutama tulemuse ekraanile.

from math import ceil
pikkus = int(input("Palun sisesta liini pikkus (täisarvuna meetrites): "))
max_kaugus = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))

postide_arv = ceil(pikkus/max_kaugus) + 1 # stardipost

print(postide_arv)
             