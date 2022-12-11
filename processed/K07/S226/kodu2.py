# import re
kilomeetrite_arv = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", encoding="UTF-8")
# data = fail.read()
taksode_hinnad = []
for rida in fail:
#     fail.readline().strip()
    rida = rida.split(",")
    stardihind = rida[1]
    stardihind = float(stardihind)
    kilomeetri_tasu = rida[2]
    kilomeetri_tasu = float(kilomeetri_tasu)
    hind = stardihind + kilomeetrite_arv*kilomeetri_tasu
    taksode_hinnad.append(hind)
#     print(hind)


väiksem = min(taksode_hinnad)
indeks = taksode_hinnad.index(väiksem)
if indeks == 0:
    print("Kõige odavam takso Maksitaksi.")
elif indeks == 1:
    print("Kõige odavam takso 'Sõps veab'.")
elif indeks == 2:
    print("Kõige odavam takso 'Waldo takso'.")
    
# something = []
# something.append(data)

# for some_el in something:
#     something_new = some_el.split(",")
# #     
# 
# print(something)
# print(something_new)

# for rida in fail:
#     fail.readline().strip()
#     faili_järjend = rida.split(",")
# 
