f = open("taksohinnad.txt", encoding = "UTF-8")

kilomeetrid = float(input("Sisesta tee pikkus koju kilomeetrites: "))

soodsaim_sõidu_hind = float("inf")
soodsaim_takso = ""
for rida in f:

    järjend = rida.split(",")
    takso = järjend[0]
    sisseistumise_hind = float(järjend[1])
    kilomeetri_hind = float(järjend[2])
    sõidu_hind = sisseistumise_hind + kilomeetrid*kilomeetri_hind
    if sõidu_hind < soodsaim_sõidu_hind:
        soodsaim_sõidu_hind = sõidu_hind
        soodsaim_takso = takso
    else:
        continue

print(soodsaim_takso) 

f.close()