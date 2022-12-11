kilomeetrite_arv = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")

nimed = []
takso_hinnad = []
uus_järjend = []
for rida in f:
    järjend = rida.split(",")
    nimi = järjend[0]
    stardihind = float(järjend[1])
    kilomeetri_hind = float(järjend[2])
    
    takso_hind = stardihind + kilomeetrite_arv * kilomeetri_hind
    takso_hinnad.append(takso_hind)
    nimed.append(nimi)
    uus_järjend.append(nimi)
    uus_järjend.append(takso_hind)
    if rida == "":
        break
    
    
väikseim = min(takso_hinnad)
indeks = uus_järjend.index(väikseim)
nime_indeks = indeks - 1
    

print("Kõige odavam on", uus_järjend[nime_indeks] + ".")

f.close()